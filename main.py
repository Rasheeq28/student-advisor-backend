
# from fastapi import FastAPI, Request, HTTPException, UploadFile, File, Form
# from fastapi.responses import JSONResponse
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel, Field
# from dotenv import load_dotenv
# import os
# import json
# from typing import Optional, List
#
# # Load environment variables from .env file (good practice for future API keys)
# load_dotenv()
#
# app = FastAPI()
#
# # --- CORS Configuration ---
# # This is CRUCIAL for frontend-backend communication when they are on different origins (ports/domains).
# # Add the exact URL(s) where your frontend is running (e.g., from VS Code's Live Server).
# origins = [
#     "http://localhost",
#     "http://localhost:5500", # Common for VS Code Live Server
#     "http://127.0.0.1:5500", # Another common Live Server address
#     # IMPORTANT: When you deploy your frontend, add its production URL here (e.g., "https://your-frontend-app.web.app")
# ]
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"], # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
#     allow_headers=["*"], # Allows all headers
# )
#
# # Define the Pydantic model for student profile data
# class StudentProfile(BaseModel):
#     studentName: str = Field(..., description="Name of the student")
#     university: str = Field(..., description="University the student attends")
#     date_of_birth: str = Field(..., description="Student's date of birth in YYYY-MM-DD format")
#     email: str = Field(..., description="Student's email address")
#     interests_and_hobbies: str = Field(..., description="Student's interests and hobbies, combined")
#     goals: str = Field(..., description="Student's academic, career, and personal goals")
#     strong_suits: str = Field(..., description="Student's strong suits, skills, or subjects they excel in")
#     weak_points: Optional[str] = Field(None, description="Student's weak points or areas for improvement (optional)")
#
# # Define the Pydantic model for the AI's recommendations (still useful for dummy structure)
# class Recommendation(BaseModel):
#     title: str
#     description: str
#     platform: Optional[str] = None # For courses
#     source: Optional[str] = None    # For lectures
#     type: Optional[str] = None      # For resources
#     link: Optional[str] = None      # Optional link for all types
#
# class AIResponse(BaseModel):
#     courses: List[Recommendation]
#     lectures: List[Recommendation]
#     resources: List[Recommendation]
#     feedback: str
#
# # --- Test Endpoint (for debugging server startup) ---
# # You can visit http://localhost:8000/ in your browser to check if the backend is running.
# @app.get("/")
# async def read_root():
#     return {"message": "FastAPI is running! Backend is alive."}
#
#
# # --- API Endpoint to Receive Student Data ---
# # This endpoint will receive the form submission from your frontend.
# @app.post("/api/submit_profile")
# async def submit_profile(
#     student_name: str = Form(...), # Changed from studentName to student_name
#     university: str = Form(...),
#     date_of_birth: str = Form(...),
#     email: str = Form(...),
#     interests_and_hobbies: str = Form(...), # Now expecting this single field
#     goals: str = Form(...),
#     strong_suits: str = Form(...),
#     weak_points: Optional[str] = Form(None),
#     cv_upload: Optional[UploadFile] = File(None) # Optional file upload field
# ):
#     """
#     Receives student profile data from the frontend, prints it to the terminal,
#     and returns dummy recommendations.
#     No LLM integration in this version.
#     """
#     try:
#         # Collect all student data from the form fields
#         student_data = {
#             "student_name": student_name, # Changed from studentName to student_name
#             "university": university,
#             "date_of_birth": date_of_birth,
#             "email": email,
#             "interests_and_hobbies": interests_and_hobbies,
#             "goals": goals,
#             "strong_suits": strong_suits,
#             "weak_points": weak_points,
#             # For CV, we'll just return the filename if a file was uploaded
#             "cv_filename": cv_upload.filename if cv_upload and cv_upload.filename else None
#         }
#
#         # --- Print the received data to your PyCharm terminal for verification ---
#         print("\n--- Received student data from frontend ---")
#         print(json.dumps(student_data, indent=2)) # Pretty print the dictionary
#         if cv_upload and cv_upload.filename:
#             print(f"Received CV file: {cv_upload.filename} (Content Type: {cv_upload.content_type})")
#             # If you want to see the file content (for small files only, for debugging):
#             # file_content = await cv_upload.read()
#             # print(f"CV content length: {len(file_content)} bytes")
#         print("-------------------------------------------\n")
#
#
#         # --- Dummy Recommendations (to match frontend's expected structure) ---
#         # The frontend JavaScript expects a 'recommendations' object with 'courses', 'lectures', 'resources', and 'feedback'.
#         # This dummy data ensures the frontend can display something without errors.
#         recommendations = {
#             "courses": [
#                 {"title": "Dummy Course: Introduction to Data Science", "description": "Learn the basics of data analysis and machine learning.", "platform": "Coursera", "link": "https://www.coursera.org/"},
#                 {"title": "Dummy Course: Advanced Python Programming", "description": "Deep dive into Python for complex applications.", "platform": "edX", "link": "https://www.edx.org/"}
#             ],
#             "lectures": [
#                 {"title": "Dummy Lecture: The Power of Critical Thinking", "description": "A lecture on developing strong analytical skills.", "source": "TED Talks", "link": "https://www.ted.com/talks"},
#                 {"title": "Dummy Lecture: Entrepreneurship 101", "description": "Insights into starting and scaling a business.", "source": "Stanford Online", "link": "https://online.stanford.edu/"}
#             ],
#             "resources": [
#                 {"title": "Dummy Resource: 'Atomic Habits' by James Clear", "description": "A book about building good habits and breaking bad ones.", "type": "Book", "link": "https://jamesclear.com/atomic-habits"},
#                 {"title": "Dummy Resource: GitHub", "description": "A platform for version control and collaboration on code.", "type": "Tool", "link": "https://github.com/"}
#             ],
#             "feedback": "This is general academic and future prospect advice from the dummy backend. Your profile data was successfully received, including your combined interests and hobbies: " + interests_and_hobbies + ". You can now see how your information is being processed!"
#         }
#
#         # Return a JSON response to the frontend.
#         # The frontend will receive this and use 'recommendations' to update the display.
#         return JSONResponse(content={
#             "message": "Profile data received and processed (no LLM yet).",
#             "received_data": student_data, # You can inspect this in your browser's console
#             "recommendations": recommendations # This is the data the frontend will display
#         })
#
#     except HTTPException as e:
#         # FastAPI's way of handling HTTP errors (e.g., validation errors)
#         print(f"HTTP Exception: {e.detail}")
#         return JSONResponse(status_code=e.status_code, content={"detail": e.detail})
#     except Exception as e:
#         # Catch any other unexpected errors
#         print(f"An unexpected error occurred in backend: {e}")
#         return JSONResponse(status_code=500, content={"detail": f"An internal server error occurred: {e}"})



# cv upload not working
# from fastapi import FastAPI, Request, HTTPException, UploadFile, File, Form
# from fastapi.responses import JSONResponse
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel, Field
# from dotenv import load_dotenv
# import os
# import json
# from typing import Optional, List
#
# # Load environment variables from .env file (good practice for future API keys)
# load_dotenv()
#
# app = FastAPI()
#
# # --- CORS Configuration ---
# # This is CRUCIAL for frontend-backend communication when they are on different origins (ports/domains).
# # Add the exact URL(s) where your frontend is running (e.g., from VS Code's Live Server).
# origins = [
#     "http://localhost",
#     "http://localhost:5500", # Common for VS Code Live Server
#     "http://127.0.0.1:5500", # Another common Live Server address
#     # IMPORTANT: When you deploy your frontend, add its production URL here (e.g., "https://your-frontend-app.web.app")
# ]
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"], # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
#     allow_headers=["*"], # Allows all headers
# )
#
# # Define the Pydantic model for student profile data
# class StudentProfile(BaseModel):
#     studentName: str = Field(..., description="Name of the student")
#     university: str = Field(..., description="University the student attends")
#     date_of_birth: str = Field(..., description="Student's date of birth in YYYY-MM-DD format")
#     email: str = Field(..., description="Student's email address")
#     interests_and_hobbies: str = Field(..., description="Student's interests and hobbies, combined")
#     goals: str = Field(..., description="Student's academic, career, and personal goals")
#     strong_suits: str = Field(..., description="Student's strong suits, skills, or subjects they excel in")
#     weak_points: Optional[str] = Field(None, description="Student's weak points or areas for improvement (optional)")
#
# # Define the Pydantic model for the AI's recommendations (still useful for dummy structure)
# class Recommendation(BaseModel):
#     title: str
#     description: str
#     platform: Optional[str] = None # For courses
#     source: Optional[str] = None    # For lectures
#     type: Optional[str] = None      # For resources
#     link: Optional[str] = None      # Optional link for all types
#
# class AIResponse(BaseModel):
#     courses: List[Recommendation]
#     lectures: List[Recommendation]
#     resources: List[Recommendation]
#     feedback: str
#
# # --- Test Endpoint (for debugging server startup) ---
# # You can visit http://localhost:8000/ in your browser to check if the backend is running.
# @app.get("/")
# async def read_root():
#     return {"message": "FastAPI is running! Backend is alive."}
#
#
# # --- API Endpoint to Receive Student Data ---
# # This endpoint will receive the form submission from your frontend.
# @app.post("/api/submit_profile")
# async def submit_profile(
#     student_name: str = Form(...),
#     university: str = Form(...),
#     date_of_birth: str = Form(...),
#     email: str = Form(...),
#     interests_and_hobbies: str = Form(...),
#     goals: str = Form(...),
#     strong_suits: str = Form(...),
#     weak_points: Optional[str] = Form(None),
#     cv_upload: Optional[UploadFile] = File(None) # Optional file upload field
# ):
#     """
#     Receives student profile data from the frontend, prints it to the terminal,
#     and returns dummy recommendations.
#     No LLM integration in this version.
#     """
#     try:
#         # Collect all student data from the form fields
#         student_data = {
#             "student_name": student_name,
#             "university": university,
#             "date_of_birth": date_of_birth,
#             "email": email,
#             "interests_and_hobbies": interests_and_hobbies,
#             "goals": goals,
#             "strong_suits": strong_suits,
#             "weak_points": weak_points,
#         }
#
#         # Conditionally add cv_filename only if a file was uploaded
#         if cv_upload and cv_upload.filename:
#             student_data["cv_filename"] = cv_upload.filename
#             print(f"Received CV file: {cv_upload.filename} (Content Type: {cv_upload.content_type})")
#             # If you want to see the file content (for small files only, for debugging):
#             # file_content = await cv_upload.read()
#             # print(f"CV content length: {len(file_content)} bytes")
#         else:
#             print("No CV file uploaded.")
#
#
#         # --- Print the received data to your PyCharm terminal for verification ---
#         print("\n--- Received student data from frontend ---")
#         print(json.dumps(student_data, indent=2)) # Pretty print the dictionary
#         print("-------------------------------------------\n")
#
#
#         # --- Dummy Recommendations (to match frontend's expected structure) ---
#         # The frontend JavaScript expects a 'recommendations' object with 'courses', 'lectures', 'resources', and 'feedback'.
#         # This dummy data ensures the frontend can display something without errors.
#         recommendations = {
#             "courses": [
#                 {"title": "Dummy Course: Introduction to Data Science", "description": "Learn the basics of data analysis and machine learning.", "platform": "Coursera", "link": "https://www.coursera.org/"},
#                 {"title": "Dummy Course: Advanced Python Programming", "description": "Deep dive into Python for complex applications.", "platform": "edX", "link": "https://www.edx.org/"}
#             ],
#             "lectures": [
#                 {"title": "Dummy Lecture: The Power of Critical Thinking", "description": "A lecture on developing strong analytical skills.", "source": "TED Talks", "link": "https://www.ted.com/talks"},
#                 {"title": "Dummy Lecture: Entrepreneurship 101", "description": "Insights into starting and scaling a business.", "source": "Stanford Online", "link": "https://online.stanford.edu/"}
#             ],
#             "resources": [
#                 {"title": "Dummy Resource: 'Atomic Habits' by James Clear", "description": "A book about building good habits and breaking bad ones.", "type": "Book", "link": "https://jamesclear.com/atomic-habits"},
#                 {"title": "Dummy Resource: GitHub", "description": "A platform for version control and collaboration on code.", "type": "Tool", "link": "https://github.com/"}
#             ],
#             "feedback": "This is general academic and future prospect advice from the dummy backend. Your profile data was successfully received, including your combined interests and hobbies: " + interests_and_hobbies + ". You can now see how your information is being processed!"
#         }
#
#         # Return a JSON response to the frontend.
#         # The frontend will receive this and use 'recommendations' to update the display.
#         return JSONResponse(content={
#             "message": "Profile data received and processed (no LLM yet).",
#             "received_data": student_data, # You can inspect this in your browser's console
#             "recommendations": recommendations # This is the data the frontend will display
#         })
#
#     except HTTPException as e:
#         # FastAPI's way of handling HTTP errors (e.g., validation errors)
#         print(f"HTTP Exception: {e.detail}")
#         return JSONResponse(status_code=e.status_code, content={"detail": e.detail})
#     except Exception as e:
#         # Catch any other unexpected errors
#         print(f"An unexpected error occurred in backend: {e}")
#         return JSONResponse(status_code=500, content={"detail": f"An internal server error occurred: {e}"})


#cv upload works
# from fastapi import FastAPI, Request, HTTPException, UploadFile, File, Form
# from fastapi.responses import JSONResponse
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel, Field
# from dotenv import load_dotenv
# import os
# import json
# from typing import Optional, List
#
# # Load environment variables from .env file (good practice for future API keys)
# load_dotenv()
#
# app = FastAPI()
#
# # --- CORS Configuration ---
# # This is CRUCIAL for frontend-backend communication when they are on different origins (ports/domains).
# # Add the exact URL(s) where your frontend is running (e.g., from VS Code's Live Server).
# origins = [
#     "http://localhost",
#     "http://localhost:5500",  # Common for VS Code Live Server
#     "http://127.0.0.1:5500",  # Another common Live Server address
#     # IMPORTANT: When you deploy your frontend, add its production URL here (e.g., "https://your-frontend-app.web.app")
# ]
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],  # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
#     allow_headers=["*"],  # Allows all headers
# )
#
#
# # Define the Pydantic model for student profile data
# class StudentProfile(BaseModel):
#     studentName: str = Field(..., description="Name of the student")
#     university: str = Field(..., description="University the student attends")
#     date_of_birth: str = Field(..., description="Student's date of birth in YYYY-MM-DD format")
#     email: str = Field(..., description="Student's email address")
#     interests_and_hobbies: str = Field(..., description="Student's interests and hobbies, combined")
#     goals: str = Field(..., description="Student's academic, career, and personal goals")
#     strong_suits: str = Field(..., description="Student's strong suits, skills, or subjects they excel in")
#     weak_points: Optional[str] = Field(None, description="Student's weak points or areas for improvement (optional)")
#
#
# # Define the Pydantic model for the AI's recommendations (still useful for dummy structure)
# class Recommendation(BaseModel):
#     title: str
#     description: str
#     platform: Optional[str] = None  # For courses
#     source: Optional[str] = None  # For lectures
#     type: Optional[str] = None  # For resources
#     link: Optional[str] = None  # Optional link for all types
#
#
# class AIResponse(BaseModel):
#     courses: List[Recommendation]
#     lectures: List[Recommendation]
#     resources: List[Recommendation]
#     feedback: str
#
#
# # --- Test Endpoint (for debugging server startup) ---
# # You can visit http://localhost:8000/ in your browser to check if the backend is running.
# @app.get("/")
# async def read_root():
#     return {"message": "FastAPI is running! Backend is alive."}
#
#
# # --- API Endpoint to Receive Student Data ---
# # This endpoint will receive the form submission from your frontend.
# @app.post("/api/submit_profile")
# async def submit_profile(
#         student_name: str = Form(...),
#         university: str = Form(...),
#         date_of_birth: str = Form(...),
#         email: str = Form(...),
#         interests_and_hobbies: str = Form(...),
#         goals: str = Form(...),
#         strong_suits: str = Form(...),
#         weak_points: Optional[str] = Form(None),
#         cv_upload: Optional[UploadFile] = File(None)  # Optional file upload field
# ):
#     """
#     Receives student profile data from the frontend, prints it to the terminal,
#     and returns dummy recommendations.
#     No LLM integration in this version.
#     """
#     try:
#         # Collect all student data from the form fields
#         student_data = {
#             "student_name": student_name,
#             "university": university,
#             "date_of_birth": date_of_birth,
#             "email": email,
#             "interests_and_hobbies": interests_and_hobbies,
#             "goals": goals,
#             "strong_suits": strong_suits,
#             "weak_points": weak_points,
#         }
#
#         # Conditionally add cv_filename only if a file was uploaded
#         if cv_upload and cv_upload.filename:
#             student_data["cv_filename"] = cv_upload.filename
#             print(f"Received CV file: {cv_upload.filename} (Content Type: {cv_upload.content_type})")
#             # If you want to see the file content (for small files only, for debugging):
#             # file_content = await cv_upload.read()
#             # print(f"CV content length: {len(file_content)} bytes")
#         else:
#             print("No CV file uploaded.")
#
#         # --- Print the received data to your PyCharm terminal for verification ---
#         print("\n--- Received student data from frontend ---")
#         print(json.dumps(student_data, indent=2))  # Pretty print the dictionary
#         print("-------------------------------------------\n")
#
#         # --- Dummy Recommendations (to match frontend's expected structure) ---
#         # The frontend JavaScript expects a 'recommendations' object with 'courses', 'lectures', 'resources', and 'feedback'.
#         # This dummy data ensures the frontend can display something without errors.
#         recommendations = {
#             "courses": [
#                 {"title": "Dummy Course: Introduction to Data Science",
#                  "description": "Learn the basics of data analysis and machine learning.", "platform": "Coursera",
#                  "link": "https://www.coursera.org/"},
#                 {"title": "Dummy Course: Advanced Python Programming",
#                  "description": "Deep dive into Python for complex applications.", "platform": "edX",
#                  "link": "https://www.edx.org/"}
#             ],
#             "lectures": [
#                 {"title": "Dummy Lecture: The Power of Critical Thinking",
#                  "description": "A lecture on developing strong analytical skills.", "source": "TED Talks",
#                  "link": "https://www.ted.com/talks"},
#                 {"title": "Dummy Lecture: Entrepreneurship 101",
#                  "description": "Insights into starting and scaling a business.", "source": "Stanford Online",
#                  "link": "https://online.stanford.edu/"}
#             ],
#             "resources": [
#                 {"title": "Dummy Resource: 'Atomic Habits' by James Clear",
#                  "description": "A book about building good habits and breaking bad ones.", "type": "Book",
#                  "link": "https://jamesclear.com/atomic-habits"},
#                 {"title": "Dummy Resource: GitHub",
#                  "description": "A platform for version control and collaboration on code.", "type": "Tool",
#                  "link": "https://github.com/"}
#             ],
#             "feedback": "This is general academic and future prospect advice from the dummy backend. Your profile data was successfully received, including your combined interests and hobbies: " + interests_and_hobbies + ". You can now see how your information is being processed!"
#         }
#
#         # Return a JSON response to the frontend.
#         # The frontend will receive this and use 'recommendations' to update the display.
#         return JSONResponse(content={
#             "message": "Profile data received and processed (no LLM yet).",
#             "received_data": student_data,  # You can inspect this in your browser's console
#             "recommendations": recommendations  # This is the data the frontend will display
#         })
#
#     except HTTPException as e:
#         # FastAPI's way of handling HTTP errors (e.g., validation errors)
#         print(f"HTTP Exception: {e.detail}")
#         return JSONResponse(status_code=e.status_code, content={"detail": e.detail})
#     except Exception as e:
#         # Catch any other unexpected errors
#         print(f"An unexpected error occurred in backend: {e}")
#         return JSONResponse(status_code=500, content={"detail": f"An internal server error occurred: {e}"})
#
#
# # --- New API Endpoint to Upload CV and Get Feedback ---
# @app.post("/api/upload_cv")
# async def upload_cv(
#         user_id: str = Form(...),  # To link CV feedback to the user
#         cv_upload: UploadFile = File(...)
# ):
#     """
#     Receives a CV file, processes it (currently returns dummy feedback),
#     and returns feedback.
#     """
#     try:
#         print(f"Received CV upload for user {user_id}: {cv_upload.filename}, Content-Type: {cv_upload.content_type}")
#
#         # In a real application, you would:
#         # 1. Save the file to a secure location (e.g., cloud storage like Supabase Storage, AWS S3).
#         # 2. Potentially send the file content to an LLM for analysis.
#         # 3. Generate actual feedback based on the analysis.
#
#         # For now, we'll just return dummy feedback.
#         dummy_feedback = f"Thank you for uploading your CV, '{cv_upload.filename}'. This is dummy feedback: Your CV looks professional! Ensure you quantify achievements and tailor it to specific job descriptions. Consider adding a strong summary statement. For more detailed feedback, please integrate a powerful LLM."
#
#         return JSONResponse(content={
#             "message": "CV received and dummy feedback generated.",
#             "filename": cv_upload.filename,
#             "feedback": dummy_feedback
#         })
#     except Exception as e:
#         print(f"Error processing CV upload: {e}")
#         raise HTTPException(status_code=500, detail=f"Failed to upload CV: {e}")



# supabase integration
from fastapi import FastAPI, Request, HTTPException, UploadFile, File, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os
import json
from typing import Optional, List
from supabase import create_client, Client
import uuid  # Import the uuid module

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# --- CORS Configuration ---
origins = [
    "http://localhost",
    "http://localhost:5500",  # Common for VS Code Live Server
    "http://127.0.0.1:5500",  # Another common Live Server address
    # IMPORTANT: When you deploy your frontend, add its production URL here (e.g., "https://your-frontend-app.web.app")
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Supabase Initialization ---
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("SUPABASE_URL and SUPABASE_KEY environment variables must be set.")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


# Define the Pydantic model for student profile data (unchanged)
class StudentProfile(BaseModel):
    studentName: str = Field(..., description="Name of the student")
    university: str = Field(..., description="University the student attends")
    date_of_birth: str = Field(..., description="Student's date of birth in YYYY-MM-DD format")
    email: str = Field(..., description="Student's email address")
    interests_and_hobbies: str = Field(..., description="Student's interests and hobbies, combined")
    goals: str = Field(..., description="Student's academic, career, and personal goals")
    strong_suits: str = Field(..., description="Student's strong suits, skills, or subjects they excel in")
    weak_points: Optional[str] = Field(None, description="Student's weak points or areas for improvement (optional)")


# Define the Pydantic model for the AI's recommendations (still useful for dummy structure)
class Recommendation(BaseModel):
    title: str
    description: str
    platform: Optional[str] = None  # For courses
    source: Optional[str] = None  # For lectures
    type: Optional[str] = None  # For resources
    link: Optional[str] = None  # Optional link for all types


class AIResponse(BaseModel):
    courses: List[Recommendation]
    lectures: List[Recommendation]
    resources: List[Recommendation]
    feedback: str


# --- Test Endpoint (for debugging server startup) ---
@app.get("/")
async def read_root():
    return {"message": "FastAPI is running! Backend is alive."}


# --- API Endpoint to Receive Student Data ---
@app.post("/api/submit_profile")
async def submit_profile(
        student_name: str = Form(...),
        university: str = Form(...),
        date_of_birth: str = Form(...),
        email: str = Form(...),
        interests_and_hobbies: str = Form(...),
        goals: str = Form(...),
        strong_suits: str = Form(...),
        weak_points: Optional[str] = Form(None),
        cv_upload: Optional[UploadFile] = File(None)  # Optional file upload field
):
    """
    Receives student profile data from the frontend, stores it in Supabase (profiles table only),
    and returns dummy recommendations.
    """
    try:
        # Generate a UUID for the user_id
        generated_user_id = str(uuid.uuid4())
        print(f"Generated user_id: {generated_user_id}")

        # Collect all student data from the form fields
        student_data = {
            "user_id": generated_user_id, # Use the generated UUID here
            "student_name": student_name,
            "university": university,
            "date_of_birth": date_of_birth,
            "email": email,
            "interests_and_hobbies": interests_and_hobbies,
            "goals": goals,
            "strong_suits": strong_suits,
            "weak_points": weak_points,
        }

        # --- Store Student Profile Data in Supabase ---
        # Insert into 'profiles' table
        response = supabase.table('profiles').insert(student_data).execute()
        if response.data:
            profile_id = response.data[0]['id']
            print(f"Student profile saved to Supabase with ID: {profile_id}")
        else:
            print(f"Failed to save student profile to Supabase: {response.error}")
            raise HTTPException(status_code=500, detail="Failed to save student profile.")

        # Conditionally add cv_filename only if a file was uploaded (for logging/debugging)
        if cv_upload and cv_upload.filename:
            student_data["cv_filename"] = cv_upload.filename
            print(f"Received CV file: {cv_upload.filename} (Content Type: {cv_upload.content_type})")
        else:
            print("No CV file uploaded with main form submission.")

        # --- Print the received data to your PyCharm terminal for verification ---
        print("\n--- Received student data from frontend ---")
        print(json.dumps(student_data, indent=2))
        print("-------------------------------------------\n")

        # --- Dummy Recommendations (to match frontend's expected structure) ---
        recommendations = {
            "courses": [
                {"title": "Dummy Course: Introduction to Data Science",
                 "description": "Learn the basics of data analysis and machine learning.", "platform": "Coursera",
                 "link": "https://www.coursera.org/"},
                {"title": "Dummy Course: Advanced Python Programming",
                 "description": "Deep dive into Python for complex applications.", "platform": "edX",
                 "link": "https://www.edx.org/"}
            ],
            "lectures": [
                {"title": "Dummy Lecture: The Power of Critical Thinking",
                 "description": "A lecture on developing strong analytical skills.", "source": "TED Talks",
                 "link": "https://www.ted.com/talks"},
                {"title": "Dummy Lecture: Entrepreneurship 101",
                 "description": "Insights into starting and scaling a business.", "source": "Stanford Online",
                 "link": "https://online.stanford.edu/"}
            ],
            "resources": [
                {"title": "Dummy Resource: 'Atomic Habits' by James Clear",
                 "description": "A book about building good habits and breaking bad ones.", "type": "Book",
                 "link": "https://jamesclear.com/atomic-habits"},
                {"title": "Dummy Resource: GitHub",
                 "description": "A platform for version control and collaboration on code.", "type": "Tool",
                 "link": "https://github.com/"}
            ],
            "feedback": "This is general academic and future prospect advice from the dummy backend. Your profile data was successfully received, including your combined interests and hobbies: " + interests_and_hobbies + ". You can now see how your information is being processed!"
        }

        # Return a JSON response to the frontend.
        return JSONResponse(content={
            "message": "Profile data received and processed (Supabase profiles integrated).",
            "received_data": student_data,
            "recommendations": recommendations
        })

    except HTTPException as e:
        print(f"HTTP Exception: {e.detail}")
        return JSONResponse(status_code=e.status_code, content={"detail": e.detail})
    except Exception as e:
        print(f"An unexpected error occurred in backend: {e}")
        return JSONResponse(status_code=500, content={"detail": f"An internal server error occurred: {e}"})


# --- API Endpoint to Upload CV and Get Feedback ---
@app.post("/api/upload_cv")
async def upload_cv(
        user_id: str = Form(...),  # Keep user_id here as it's passed from frontend for CV upload
        cv_upload: UploadFile = File(...)
):
    """
    Receives a CV file, processes it (currently returns dummy feedback),
    and returns feedback.
    """
    try:
        print(f"Received CV upload for user {user_id}: {cv_upload.filename}, Content-Type: {cv_upload.content_type}")

        # For now, we'll just return dummy feedback.
        dummy_feedback = f"Thank you for uploading your CV, '{cv_upload.filename}'. This is dummy feedback: Your CV looks professional! Ensure you quantify achievements and tailor it to specific job descriptions. Consider adding a strong summary statement. For more detailed feedback, please integrate a powerful LLM."

        return JSONResponse(content={
            "message": "CV received and dummy feedback generated.",
            "filename": cv_upload.filename,
            "feedback": dummy_feedback
        })
    except Exception as e:
        print(f"Error processing CV upload: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to upload CV: {e}")