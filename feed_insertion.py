# import streamlit as st
# from supabase import create_client
# import datetime
#
# # Load from secrets
# url = st.secrets["supabase"]["url"]
# key = st.secrets["supabase"]["key"]
#
# supabase = create_client(url, key)
#
# st.title("Admin Panel - Content Uploader")
#
# producer_name = st.text_input("Producer Name")
# img_link = st.text_input("Image Link")
# title = st.text_input("Title")
# description = st.text_area("Description")
# content_type = st.selectbox("Content Type", ["Article", "Course", "CA", "BIzcomp"])
# tags = st.text_input("Tags (comma separated)")
# date_tag = st.date_input("Date Tag")
#
# if st.button("Submit"):
#     data = {
#         "producer_name": producer_name,
#         "img_link": img_link,
#         "title": title,
#         "Description": description,
#         "content_type": content_type,
#         "tags": tags,
#         "date_tag": str(date_tag),
#     }
#
#     try:
#         response = supabase.table("Feed").insert(data).execute()
#         st.success("✅ Successfully added to Supabase!")
#     except Exception as e:
#         st.error(f"❌ Error: {e}")


# crud
# import streamlit as st
# from supabase import create_client
# import datetime
#
# # Supabase client
# url = st.secrets["supabase"]["url"]
# key = st.secrets["supabase"]["key"]
# supabase = create_client(url, key)
#
# # Streamlit layout
# st.set_page_config(page_title="Feed Admin Panel", layout="wide")
# st.title("📦 Feed Admin Panel")
#
# # Tabs for CRUD
# tab1, tab2, tab3, tab4 = st.tabs(["➕ Create", "📄 Read", "✏️ Update", "❌ Delete"])
#
# # CREATE TAB
# with tab1:
#     st.subheader("Add New Feed Entry")
#
#     producer_name = st.text_input("Producer Name")
#     img_link = st.text_input("Image Link")
#     title = st.text_input("Title")
#     description = st.text_area("Description")
#     content_type = st.selectbox("Content Type", ["Article", "Course", "CA", "BIzcomp"], key="create_content_type")
#     tags = st.text_input("Tags (comma separated)")
#     date_tag = st.date_input("Date Tag")
#
#     if st.button("Create Entry"):
#         data = {
#             "producer_name": producer_name,
#             "img_link": img_link,
#             "title": title,
#             "Description": description,
#             "content_type": content_type,
#             "tags": tags,
#             "date_tag": date_tag.isoformat(),
#         }
#         try:
#             supabase.table("Feed").insert(data).execute()
#             st.success("✅ Successfully added!")
#         except Exception as e:
#             st.error(f"❌ Error: {e}")
#
# # READ TAB
# with tab2:
#     st.subheader("All Feed Entries")
#     try:
#         res = supabase.table("Feed").select("*").order("created_at", desc=True).execute()
#         rows = res.data
#         if rows:
#             st.dataframe(rows, use_container_width=True)
#         else:
#             st.info("No entries found.")
#     except Exception as e:
#         st.error(f"❌ Error: {e}")
#
# # UPDATE TAB
# with tab3:
#     st.subheader("Update an Entry")
#
#     try:
#         entries = supabase.table("Feed").select("id, title").execute().data
#         entry_dict = {f"{e['title']} ({e['id']})": e["id"] for e in entries}
#
#         selected = st.selectbox("Select entry to update", list(entry_dict.keys()), key="update_selectbox")
#         if selected:
#             entry_id = entry_dict[selected]
#             full_entry = supabase.table("Feed").select("*").eq("id", entry_id).single().execute().data
#
#             # Editable fields
#             new_producer_name = st.text_input("Producer Name", full_entry["producer_name"], key="update_producer_name")
#             new_img_link = st.text_input("Image Link", full_entry["img_link"], key="update_img_link")
#             new_title = st.text_input("Title", full_entry["title"], key="update_title")
#             new_description = st.text_area("Description", full_entry.get("Description", ""), key="update_description")
#             new_content_type = st.selectbox(
#                 "Content Type",
#                 ["Article", "Course", "CA", "BIzcomp"],
#                 index=["Article", "Course", "CA", "BIzcomp"].index(full_entry["content_type"]),
#                 key="update_content_type"
#             )
#             new_tags = st.text_input("Tags", full_entry["tags"], key="update_tags")
#             new_date_tag = st.date_input("Date Tag", datetime.date.fromisoformat(full_entry["date_tag"]), key="update_date")
#
#             if st.button("Update Entry", key="update_button"):
#                 update_data = {
#                     "producer_name": new_producer_name,
#                     "img_link": new_img_link,
#                     "title": new_title,
#                     "Description": new_description,
#                     "content_type": new_content_type,
#                     "tags": new_tags,
#                     "date_tag": new_date_tag.isoformat()
#                 }
#
#                 supabase.table("Feed").update(update_data).eq("id", entry_id).execute()
#                 st.success("✅ Entry updated!")
#
#     except Exception as e:
#         st.error(f"❌ Error: {e}")
#
# # DELETE TAB
# with tab4:
#     st.subheader("Delete an Entry")
#     try:
#         entries = supabase.table("Feed").select("id, title").execute().data
#         entry_dict = {f"{e['title']} ({e['id']})": e["id"] for e in entries}
#
#         selected = st.selectbox("Select entry to delete", list(entry_dict.keys()), key="delete_selectbox")
#         if selected:
#             entry_id = entry_dict[selected]
#             if st.button("Delete Entry", key="delete_button"):
#                 supabase.table("Feed").delete().eq("id", entry_id).execute()
#                 st.success("✅ Entry deleted.")
#     except Exception as e:
#         st.error(f"❌ Error: {e}")


# img upload
# import streamlit as st
# from supabase import create_client
# from datetime import datetime
# import uuid
#
# # Load from secrets
# url = st.secrets["supabase"]["url"]
# key = st.secrets["supabase"]["key"]
# supabase = create_client(url, key)
#
# st.title("📚 Admin Panel - Content Manager")
#
# tabs = st.tabs(["➕ Create", "📖 Read", "📝 Update", "❌ Delete"])
#
# # ---------- CREATE ----------
# with tabs[0]:
#     st.header("Add New Content")
#
#     producer_name = st.text_input("Producer Name")
#     title = st.text_input("Title")
#     description = st.text_area("Description")
#     content_type = st.selectbox("Content Type", ["Article", "Course", "CA", "Bizcomp"], key="create_content_type")
#     tags = st.text_input("Tags (comma separated)")
#     date_tag = st.date_input("Date Tag")
#     img_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
#
#     if st.button("Submit"):
#         if img_file:
#             try:
#                 # Generate unique filename
#                 unique_filename = f"{uuid.uuid4()}_{img_file.name}"
#                 file_bytes = img_file.read()
#
#                 supabase.storage.from_("feed-img").upload(unique_filename, file_bytes)
#                 public_url = supabase.storage.from_("feed-img").get_public_url(unique_filename)
#             except Exception as e:
#                 st.error(f"❌ Upload failed: {e}")
#                 st.stop()
#         else:
#             public_url = ""
#
#         data = {
#             "producer_name": producer_name,
#             "title": title,
#             "Description": description,
#             "content_type": content_type,
#             "tags": tags,
#             "date_tag": str(date_tag),
#             "img_link": public_url,
#         }
#
#         try:
#             supabase.table("Feed").insert(data).execute()
#             st.success("✅ Content added successfully!")
#         except Exception as e:
#             st.error(f"❌ Error: {e}")
#
# # ---------- READ ----------
# with tabs[1]:
#     st.header("View All Content")
#     search_term = st.text_input("🔍 Search by title or producer name", key="read_search")
#
#     try:
#         response = supabase.table("Feed").select("*").execute()
#         records = response.data
#
#         if search_term:
#             records = [r for r in records if search_term.lower() in r["title"].lower() or search_term.lower() in r["producer_name"].lower()]
#
#         if records:
#             for record in records:
#                 st.subheader(record["title"])
#                 st.markdown(f"**Producer:** {record['producer_name']}")
#                 st.markdown(f"**Type:** {record['content_type']}")
#                 st.markdown(f"**Tags:** {record['tags']}")
#                 st.markdown(f"**Date:** {record['date_tag']}")
#                 st.markdown(f"**Description:** {record['Description']}")
#                 if record["img_link"]:
#                     st.image(record["img_link"], width=300)
#                 st.markdown("---")
#         else:
#             st.info("No records found.")
#     except Exception as e:
#         st.error(f"❌ Error: {e}")
#
# # ---------- UPDATE ----------
# with tabs[2]:
#     st.header("Update Existing Content")
#     try:
#         response = supabase.table("Feed").select("*").execute()
#         records = response.data
#         search_term = st.text_input("🔍 Search by title", key="update_search")
#
#         if search_term:
#             records = [r for r in records if search_term.lower() in r["title"].lower()]
#
#         titles = [r["title"] for r in records]
#         if titles:
#             selected_title = st.selectbox("Select a title to update", titles, key="update_title")
#             selected_record = next((r for r in records if r["title"] == selected_title), None)
#
#             if selected_record:
#                 new_title = st.text_input("Title", selected_record["title"])
#                 new_description = st.text_area("Description", selected_record["Description"])
#                 new_tags = st.text_input("Tags", selected_record["tags"])
#                 new_date_tag = st.date_input("Date Tag", datetime.strptime(selected_record["date_tag"], "%Y-%m-%d"))
#                 new_type = st.selectbox("Content Type", ["Article", "Course", "CA", "Bizcomp"], index=["Article", "Course", "CA", "Bizcomp"].index(selected_record["content_type"]), key="update_type")
#                 new_img = st.file_uploader("New Image (optional)", key="update_img")
#
#                 if st.button("Update"):
#                     update_data = {
#                         "title": new_title,
#                         "Description": new_description,
#                         "tags": new_tags,
#                         "date_tag": str(new_date_tag),
#                         "content_type": new_type,
#                     }
#
#                     if new_img:
#                         unique_filename = f"{uuid.uuid4()}_{new_img.name}"
#                         file_bytes = new_img.read()
#                         supabase.storage.from_("feed-img").upload(unique_filename, file_bytes)
#                         public_url = supabase.storage.from_("feed-img").get_public_url(unique_filename)
#                         update_data["img_link"] = public_url
#
#                     supabase.table("Feed").update(update_data).eq("id", selected_record["id"]).execute()
#                     st.success("✅ Content updated successfully!")
#         else:
#             st.info("No records found.")
#     except Exception as e:
#         st.error(f"❌ Error: {e}")
#
# # ---------- DELETE ----------
# with tabs[3]:
#     st.header("Delete Content")
#     try:
#         response = supabase.table("Feed").select("*").execute()
#         records = response.data
#         titles = [r["title"] for r in records]
#         selected_title = st.selectbox("Select a title to delete", titles, key="delete_title")
#         selected_record = next((r for r in records if r["title"] == selected_title), None)
#
#         if st.button("Delete"):
#             supabase.table("Feed").delete().eq("id", selected_record["id"]).execute()
#             st.success("🗑️ Deleted successfully!")
#     except Exception as e:
#         st.error(f"❌ Error: {e}")


# fixed search
# import streamlit as st
# from supabase import create_client
# from datetime import datetime
# import uuid
#
# # Load from secrets
# url = st.secrets["supabase"]["url"]
# key = st.secrets["supabase"]["key"]
# supabase = create_client(url, key)
#
# st.title("📚 Admin Panel - Content Manager")
#
# tabs = st.tabs(["➕ Create", "📖 Read", "📝 Update", "❌ Delete"])
#
# # ---------- CREATE ----------
# with tabs[0]:
#     st.header("Add New Content")
#
#     producer_name = st.text_input("Producer Name")
#     title = st.text_input("Title")
#     description = st.text_area("Description")
#     content_type = st.selectbox("Content Type", ["Article", "Course", "CA", "Bizcomp"], key="create_content_type")
#     tags = st.text_input("Tags (comma separated)")
#     date_tag = st.date_input("Date Tag")
#     img_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
#
#     if st.button("Submit"):
#         if img_file:
#             try:
#                 # Generate unique filename
#                 unique_filename = f"{uuid.uuid4()}_{img_file.name}"
#                 file_bytes = img_file.read()
#                 supabase.storage.from_("feed-img").upload(unique_filename, file_bytes)
#                 public_url = supabase.storage.from_("feed-img").get_public_url(unique_filename)
#             except Exception as e:
#                 st.error(f"❌ Upload failed: {e}")
#                 st.stop()
#         else:
#             public_url = ""
#
#         data = {
#             "producer_name": producer_name,
#             "title": title,
#             "Description": description,
#             "content_type": content_type,
#             "tags": tags,
#             "date_tag": str(date_tag),
#             "img_link": public_url,
#         }
#
#         try:
#             supabase.table("Feed").insert(data).execute()
#             st.success("✅ Content added successfully!")
#         except Exception as e:
#             st.error(f"❌ Error: {e}")
#
# # ---------- READ ----------
# with tabs[1]:
#     st.header("View All Content")
#     search_term = st.text_input("🔍 Search by title or producer name", key="read_search")
#
#     try:
#         response = supabase.table("Feed").select("*").execute()
#         records = response.data
#
#         if search_term:
#             records = [r for r in records if search_term.lower() in r["title"].lower() or search_term.lower() in r["producer_name"].lower()]
#
#         if records:
#             for record in records:
#                 st.subheader(record["title"])
#                 st.markdown(f"**Producer:** {record['producer_name']}")
#                 st.markdown(f"**Type:** {record['content_type']}")
#                 st.markdown(f"**Tags:** {record['tags']}")
#                 st.markdown(f"**Date:** {record['date_tag']}")
#                 st.markdown(f"**Description:** {record['Description']}")
#                 if record["img_link"]:
#                     st.image(record["img_link"], width=300)
#                 st.markdown("---")
#         else:
#             st.info("No records found.")
#     except Exception as e:
#         st.error(f"❌ Error: {e}")
#
# # ---------- UPDATE ----------
# with tabs[2]:
#     st.header("Update Existing Content")
#     try:
#         response = supabase.table("Feed").select("*").execute()
#         records = response.data
#         search_term = st.text_input("🔍 Search by producer name", key="update_search")
#
#         if search_term:
#             records = [r for r in records if search_term.lower() in r["producer_name"].lower()]
#
#         producers = [f"{r['producer_name']} - {r['title']}" for r in records]
#         if producers:
#             selected_display = st.selectbox("Select content by producer", producers, key="update_selectbox")
#             selected_record = next((r for r in records if f"{r['producer_name']} - {r['title']}" == selected_display), None)
#
#             if selected_record:
#                 new_title = st.text_input("Title", selected_record["title"])
#                 new_description = st.text_area("Description", selected_record["Description"])
#                 new_tags = st.text_input("Tags", selected_record["tags"])
#                 new_date_tag = st.date_input("Date Tag", datetime.strptime(selected_record["date_tag"], "%Y-%m-%d"))
#                 new_type = st.selectbox("Content Type", ["Article", "Course", "CA", "Bizcomp"], index=["Article", "Course", "CA", "Bizcomp"].index(selected_record["content_type"]), key="update_type")
#                 new_img = st.file_uploader("New Image (optional)", key="update_img")
#
#                 if st.button("Update"):
#                     update_data = {
#                         "title": new_title,
#                         "Description": new_description,
#                         "tags": new_tags,
#                         "date_tag": str(new_date_tag),
#                         "content_type": new_type,
#                     }
#
#                     if new_img:
#                         unique_filename = f"{uuid.uuid4()}_{new_img.name}"
#                         file_bytes = new_img.read()
#                         supabase.storage.from_("feed-img").upload(unique_filename, file_bytes)
#                         public_url = supabase.storage.from_("feed-img").get_public_url(unique_filename)
#                         update_data["img_link"] = public_url
#
#                     supabase.table("Feed").update(update_data).eq("id", selected_record["id"]).execute()
#                     st.success("✅ Content updated successfully!")
#         else:
#             st.info("No records found.")
#     except Exception as e:
#         st.error(f"❌ Error: {e}")
#
# # ---------- DELETE ----------
# with tabs[3]:
#     st.header("Delete Content")
#     try:
#         response = supabase.table("Feed").select("*").execute()
#         records = response.data
#         search_term = st.text_input("🔍 Search by producer name", key="delete_search")
#
#         if search_term:
#             records = [r for r in records if search_term.lower() in r["producer_name"].lower()]
#
#         producers = [f"{r['producer_name']} - {r['title']}" for r in records]
#         selected_display = st.selectbox("Select content to delete", producers, key="delete_selectbox")
#         selected_record = next((r for r in records if f"{r['producer_name']} - {r['title']}" == selected_display), None)
#
#         if st.button("Delete"):
#             supabase.table("Feed").delete().eq("id", selected_record["id"]).execute()
#             st.success("🗑️ Deleted successfully!")
#     except Exception as e:
#         st.error(f"❌ Error: {e}")


# login methods
# import streamlit as st
# from supabase import create_client
# from datetime import datetime
# import uuid
# import requests
#
# # Load from secrets
# SUPABASE_URL = st.secrets["supabase"]["url"]
# SERVICE_ROLE_KEY = st.secrets["supabase"]["service_role_key"]  # Must be service role key!
# supabase = create_client(SUPABASE_URL, SERVICE_ROLE_KEY)
#
# HEADERS = {
#     "apikey": SERVICE_ROLE_KEY,
#     "Authorization": f"Bearer {SERVICE_ROLE_KEY}",
#     "Content-Type": "application/json",
# }
#
# # --- Admin API helper functions ---
# def create_user(email, password):
#     url = f"{SUPABASE_URL}/auth/v1/admin/users"
#     payload = {
#         "email": email,
#         "password": password,
#         "email_confirm": True
#     }
#     r = requests.post(url, json=payload, headers=HEADERS)
#     return r.json()
#
# def update_user(user_id, email=None, password=None):
#     url = f"{SUPABASE_URL}/auth/v1/admin/users/{user_id}"
#     payload = {}
#     if email:
#         payload["email"] = email
#     if password:
#         payload["password"] = password
#     r = requests.put(url, json=payload, headers=HEADERS)
#     return r.json()
#
# def delete_user(user_id):
#     url = f"{SUPABASE_URL}/auth/v1/admin/users/{user_id}"
#     r = requests.delete(url, headers=HEADERS)
#     return r.json()
#
# # ----------- Streamlit UI -----------
#
# st.title("📚 Admin Panel - Content Manager")
#
# tabs = st.tabs(["➕ Create", "📖 Read", "📝 Update", "❌ Delete", "👤 Users"])
#
# # ---------- CREATE ----------
# with tabs[0]:
#     st.header("Add New Content")
#
#     producer_name = st.text_input("Producer Name")
#     title = st.text_input("Title")
#     description = st.text_area("Description")
#     content_type = st.selectbox("Content Type", ["Article", "Course", "CA", "Bizcomp"], key="create_content_type")
#     tags = st.text_input("Tags (comma separated)")
#     date_tag = st.date_input("Date Tag")
#     img_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
#
#     if st.button("Submit"):
#         if img_file:
#             try:
#                 unique_filename = f"{uuid.uuid4()}_{img_file.name}"
#                 file_bytes = img_file.read()
#                 supabase.storage.from_("feed-img").upload(unique_filename, file_bytes)
#                 public_url = supabase.storage.from_("feed-img").get_public_url(unique_filename)
#             except Exception as e:
#                 st.error(f"❌ Upload failed: {e}")
#                 st.stop()
#         else:
#             public_url = ""
#
#         data = {
#             "producer_name": producer_name,
#             "title": title,
#             "Description": description,
#             "content_type": content_type,
#             "tags": tags,
#             "date_tag": str(date_tag),
#             "img_link": public_url,
#         }
#
#         try:
#             supabase.table("Feed").insert(data).execute()
#             st.success("✅ Content added successfully!")
#         except Exception as e:
#             st.error(f"❌ Error: {e}")
#
# # ---------- READ ----------
# with tabs[1]:
#     st.header("View All Content")
#     search_term = st.text_input("🔍 Search by title or producer name", key="read_search")
#
#     try:
#         response = supabase.table("Feed").select("*").execute()
#         records = response.data
#
#         if search_term:
#             records = [r for r in records if search_term.lower() in r["title"].lower() or search_term.lower() in r["producer_name"].lower()]
#
#         if records:
#             for record in records:
#                 st.subheader(record["title"])
#                 st.markdown(f"**Producer:** {record['producer_name']}")
#                 st.markdown(f"**Type:** {record['content_type']}")
#                 st.markdown(f"**Tags:** {record['tags']}")
#                 st.markdown(f"**Date:** {record['date_tag']}")
#                 st.markdown(f"**Description:** {record['Description']}")
#                 if record["img_link"]:
#                     st.image(record["img_link"], width=300)
#                 st.markdown("---")
#         else:
#             st.info("No records found.")
#     except Exception as e:
#         st.error(f"❌ Error: {e}")
#
# # ---------- UPDATE ----------
# with tabs[2]:
#     st.header("Update Existing Content")
#     try:
#         response = supabase.table("Feed").select("*").execute()
#         records = response.data
#         search_term = st.text_input("🔍 Search by producer name", key="update_search")
#
#         if search_term:
#             records = [r for r in records if search_term.lower() in r["producer_name"].lower()]
#
#         producers = [f"{r['producer_name']} - {r['title']}" for r in records]
#         if producers:
#             selected_display = st.selectbox("Select content by producer", producers, key="update_selectbox")
#             selected_record = next((r for r in records if f"{r['producer_name']} - {r['title']}" == selected_display), None)
#
#             if selected_record:
#                 new_title = st.text_input("Title", selected_record["title"])
#                 new_description = st.text_area("Description", selected_record["Description"])
#                 new_tags = st.text_input("Tags", selected_record["tags"])
#                 new_date_tag = st.date_input("Date Tag", datetime.strptime(selected_record["date_tag"], "%Y-%m-%d"))
#                 new_type = st.selectbox("Content Type", ["Article", "Course", "CA", "Bizcomp"], index=["Article", "Course", "CA", "Bizcomp"].index(selected_record["content_type"]), key="update_type")
#                 new_img = st.file_uploader("New Image (optional)", key="update_img")
#
#                 if st.button("Update"):
#                     update_data = {
#                         "title": new_title,
#                         "Description": new_description,
#                         "tags": new_tags,
#                         "date_tag": str(new_date_tag),
#                         "content_type": new_type,
#                     }
#
#                     if new_img:
#                         unique_filename = f"{uuid.uuid4()}_{new_img.name}"
#                         file_bytes = new_img.read()
#                         supabase.storage.from_("feed-img").upload(unique_filename, file_bytes)
#                         public_url = supabase.storage.from_("feed-img").get_public_url(unique_filename)
#                         update_data["img_link"] = public_url
#
#                     supabase.table("Feed").update(update_data).eq("id", selected_record["id"]).execute()
#                     st.success("✅ Content updated successfully!")
#         else:
#             st.info("No records found.")
#     except Exception as e:
#         st.error(f"❌ Error: {e}")
#
# # ---------- DELETE ----------
# with tabs[3]:
#     st.header("Delete Content")
#     try:
#         response = supabase.table("Feed").select("*").execute()
#         records = response.data
#         search_term = st.text_input("🔍 Search by producer name", key="delete_search")
#
#         if search_term:
#             records = [r for r in records if search_term.lower() in r["producer_name"].lower()]
#
#         producers = [f"{r['producer_name']} - {r['title']}" for r in records]
#         selected_display = st.selectbox("Select content to delete", producers, key="delete_selectbox")
#         selected_record = next((r for r in records if f"{r['producer_name']} - {r['title']}" == selected_display), None)
#
#         if st.button("Delete"):
#             supabase.table("Feed").delete().eq("id", selected_record["id"]).execute()
#             st.success("🗑️ Deleted successfully!")
#     except Exception as e:
#         st.error(f"❌ Error: {e}")
#
# # ---------- USERS TAB ----------
# with tabs[4]:
#     st.header("Manage Authenticated Users")
#
#     user_tabs = st.tabs(["➕ Add User", "📋 List Users", "📝 Update User", "❌ Delete User"])
#
#     # 1. Add User
#     with user_tabs[0]:
#         st.subheader("Add New User")
#         new_email = st.text_input("Email", key="new_email")
#         new_full_name = st.text_input("Full Name", key="new_full_name")
#         new_password = st.text_input("Password", type="password", key="new_password")
#
#         if st.button("Create User"):
#             if not new_email or not new_password:
#                 st.error("Email and password are required!")
#             else:
#                 try:
#                     res = create_user(new_email, new_password)
#                     if res.get("id"):
#                         user_id = res["id"]
#                         insert_res = supabase.table("authenticated_users").insert({
#                             "id": user_id,
#                             "email": new_email,
#                             "full_name": new_full_name
#                         }).execute()
#                         if insert_res.error:
#                             st.warning(f"User created but failed to add profile: {insert_res.error.message}")
#                         else:
#                             st.success(f"User created with ID: {user_id}")
#                     else:
#                         st.error(f"Failed to create user: {res}")
#                 except Exception as e:
#                     st.error(f"Exception: {e}")
#
#     # 2. List Users
#     with user_tabs[1]:
#         st.subheader("List Users")
#         try:
#             profiles_res = supabase.table("authenticated_users").select("*").execute()
#             profiles = profiles_res.data
#
#             if profiles:
#                 for p in profiles:
#                     st.markdown(f"**ID:** {p['id']}")
#                     st.markdown(f"**Email:** {p['email']}")
#                     st.markdown(f"**Full Name:** {p.get('full_name', '')}")
#                     st.markdown("---")
#             else:
#                 st.info("No users found.")
#         except Exception as e:
#             st.error(f"Error fetching users: {e}")
#
#     # 3. Update User
#     with user_tabs[2]:
#         st.subheader("Update User")
#
#         try:
#             profiles_res = supabase.table("authenticated_users").select("*").execute()
#             profiles = profiles_res.data
#
#             if profiles:
#                 user_display = [f"{p['email']} - {p.get('full_name', '')}" for p in profiles]
#                 selected_user = st.selectbox("Select user to update", user_display)
#
#                 user_obj = next((p for p in profiles if f"{p['email']} - {p.get('full_name', '')}" == selected_user), None)
#
#                 if user_obj:
#                     updated_email = st.text_input("Email", value=user_obj["email"], key="update_email")
#                     updated_full_name = st.text_input("Full Name", value=user_obj.get("full_name", ""), key="update_full_name")
#                     updated_password = st.text_input("New Password (leave blank to keep unchanged)", type="password", key="update_password")
#
#                     if st.button("Update User"):
#                         update_data = {
#                             "email": updated_email,
#                             "full_name": updated_full_name
#                         }
#                         try:
#                             update_auth_resp = update_user(user_obj["id"], email=updated_email, password=updated_password if updated_password else None)
#                             if update_auth_resp.get("id"):
#                                 update_profile_res = supabase.table("authenticated_users").update(update_data).eq("id", user_obj["id"]).execute()
#                                 if update_profile_res.error:
#                                     st.warning(f"User auth updated but profile update failed: {update_profile_res.error.message}")
#                                 else:
#                                     st.success("User updated successfully!")
#                             else:
#                                 st.error(f"Failed to update auth user: {update_auth_resp}")
#                         except Exception as e:
#                             st.error(f"Exception during update: {e}")
#             else:
#                 st.info("No users found.")
#         except Exception as e:
#             st.error(f"Error fetching users: {e}")
#
#     # 4. Delete User
#     with user_tabs[3]:
#         st.subheader("Delete User")
#         try:
#             profiles_res = supabase.table("authenticated_users").select("*").execute()
#             profiles = profiles_res.data
#
#             if profiles:
#                 user_display = [f"{p['email']} - {p.get('full_name', '')}" for p in profiles]
#                 selected_user = st.selectbox("Select user to delete", user_display)
#
#                 user_obj = next((p for p in profiles if f"{p['email']} - {p.get('full_name', '')}" == selected_user), None)
#
#                 if st.button("Delete User"):
#                     try:
#                         del_auth_resp = delete_user(user_obj["id"])
#                         if del_auth_resp == {}:  # delete returns empty dict on success
#                             del_profile_resp = supabase.table("authenticated_users").delete().eq("id", user_obj["id"]).execute()
#                             if del_profile_resp.error:
#                                 st.warning(f"Auth user deleted but profile delete failed: {del_profile_resp.error.message}")
#                             else:
#                                 st.success("User deleted successfully!")
#                         else:
#                             st.error(f"Failed to delete auth user: {del_auth_resp}")
#                     except Exception as e:
#                         st.error(f"Exception during deletion: {e}")
#             else:
#                 st.info("No users found.")
#         except Exception as e:
#             st.error(f"Error fetching users: {e}")


# loginv1
# import streamlit as st
# from supabase import create_client
# from datetime import datetime
# import uuid
# import requests
#
# # Load from secrets
# SUPABASE_URL = st.secrets["supabase"]["url"]
# SERVICE_ROLE_KEY = st.secrets["supabase"]["service_role_key"]  # Must be service role key!
# supabase = create_client(SUPABASE_URL, SERVICE_ROLE_KEY)
#
# HEADERS = {
#     "apikey": SERVICE_ROLE_KEY,
#     "Authorization": f"Bearer {SERVICE_ROLE_KEY}",
#     "Content-Type": "application/json",
# }
#
# # --- Admin API helper functions ---
# def create_user(email, password):
#     url = f"{SUPABASE_URL}/auth/v1/admin/users"
#     payload = {
#         "email": email,
#         "password": password,
#         "email_confirm": True
#     }
#     r = requests.post(url, json=payload, headers=HEADERS)
#     if r.status_code == 201:
#         return r.json()
#     else:
#         return {"error": r.json()}
#
# def update_user(user_id, email=None, password=None):
#     url = f"{SUPABASE_URL}/auth/v1/admin/users/{user_id}"
#     payload = {}
#     if email:
#         payload["email"] = email
#     if password:
#         payload["password"] = password
#     r = requests.put(url, json=payload, headers=HEADERS)
#     if r.status_code == 200:
#         return r.json()
#     else:
#         return {"error": r.json()}
#
# def delete_user(user_id):
#     url = f"{SUPABASE_URL}/auth/v1/admin/users/{user_id}"
#     r = requests.delete(url, headers=HEADERS)
#     if r.status_code == 204:
#         return {}  # success returns empty response
#     else:
#         return {"error": r.json()}
#
# # ----------- Streamlit UI -----------
#
# st.title("📚 Admin Panel - Content Manager")
#
# tabs = st.tabs(["➕ Create", "📖 Read", "📝 Update", "❌ Delete", "👤 Users"])
#
# # ---------- CREATE ----------
# with tabs[0]:
#     st.header("Add New Content")
#
#     producer_name = st.text_input("Producer Name", key="create_producer")
#     title = st.text_input("Title", key="create_title")
#     description = st.text_area("Description", key="create_description")
#     content_type = st.selectbox("Content Type", ["Article", "Course", "CA", "Bizcomp"], key="create_content_type")
#     tags = st.text_input("Tags (comma separated)", key="create_tags")
#     date_tag = st.date_input("Date Tag", key="create_date")
#     img_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"], key="create_img")
#
#     if st.button("Submit", key="create_submit"):
#         if img_file:
#             try:
#                 unique_filename = f"{uuid.uuid4()}_{img_file.name}"
#                 file_bytes = img_file.read()
#                 supabase.storage.from_("feed-img").upload(unique_filename, file_bytes)
#                 public_url = supabase.storage.from_("feed-img").get_public_url(unique_filename)
#             except Exception as e:
#                 st.error(f"❌ Upload failed: {e}")
#                 st.stop()
#         else:
#             public_url = ""
#
#         data = {
#             "producer_name": producer_name,
#             "title": title,
#             "Description": description,
#             "content_type": content_type,
#             "tags": tags,
#             "date_tag": str(date_tag),
#             "img_link": public_url,
#         }
#
#         try:
#             res = supabase.table("Feed").insert(data).execute()
#             if res.status_code >= 400:
#                 st.error(f"❌ Error: {res.data}")
#             else:
#                 st.success("✅ Content added successfully!")
#         except Exception as e:
#             st.error(f"❌ Exception: {e}")
#
# # ---------- READ ----------
# with tabs[1]:
#     st.header("View All Content")
#     search_term = st.text_input("🔍 Search by title or producer name", key="read_search")
#
#     try:
#         response = supabase.table("Feed").select("*").execute()
#         records = response.data
#
#         if search_term:
#             records = [r for r in records if search_term.lower() in r["title"].lower() or search_term.lower() in r["producer_name"].lower()]
#
#         if records:
#             for record in records:
#                 st.subheader(record["title"])
#                 st.markdown(f"**Producer:** {record['producer_name']}")
#                 st.markdown(f"**Type:** {record['content_type']}")
#                 st.markdown(f"**Tags:** {record['tags']}")
#                 st.markdown(f"**Date:** {record['date_tag']}")
#                 st.markdown(f"**Description:** {record['Description']}")
#                 if record["img_link"]:
#                     st.image(record["img_link"], width=300)
#                 st.markdown("---")
#         else:
#             st.info("No records found.")
#     except Exception as e:
#         st.error(f"❌ Error: {e}")
#
# # ---------- UPDATE ----------
# with tabs[2]:
#     st.header("Update Existing Content")
#     try:
#         response = supabase.table("Feed").select("*").execute()
#         records = response.data
#         search_term = st.text_input("🔍 Search by producer name", key="update_search")
#
#         if search_term:
#             records = [r for r in records if search_term.lower() in r["producer_name"].lower()]
#
#         producers = [f"{r['producer_name']} - {r['title']}" for r in records]
#         if producers:
#             selected_display = st.selectbox("Select content by producer", producers, key="update_selectbox")
#             selected_record = next((r for r in records if f"{r['producer_name']} - {r['title']}" == selected_display), None)
#
#             if selected_record:
#                 new_title = st.text_input("Title", selected_record["title"], key="update_title")
#                 new_description = st.text_area("Description", selected_record["Description"], key="update_description")
#                 new_tags = st.text_input("Tags", selected_record["tags"], key="update_tags")
#                 new_date_tag = st.date_input("Date Tag", datetime.strptime(selected_record["date_tag"], "%Y-%m-%d"), key="update_date")
#                 new_type = st.selectbox("Content Type", ["Article", "Course", "CA", "Bizcomp"], index=["Article", "Course", "CA", "Bizcomp"].index(selected_record["content_type"]), key="update_type")
#                 new_img = st.file_uploader("New Image (optional)", key="update_img")
#
#                 if st.button("Update", key="update_button"):
#                     update_data = {
#                         "title": new_title,
#                         "Description": new_description,
#                         "tags": new_tags,
#                         "date_tag": str(new_date_tag),
#                         "content_type": new_type,
#                     }
#
#                     if new_img:
#                         unique_filename = f"{uuid.uuid4()}_{new_img.name}"
#                         file_bytes = new_img.read()
#                         supabase.storage.from_("feed-img").upload(unique_filename, file_bytes)
#                         public_url = supabase.storage.from_("feed-img").get_public_url(unique_filename)
#                         update_data["img_link"] = public_url
#
#                     res = supabase.table("Feed").update(update_data).eq("id", selected_record["id"]).execute()
#                     if res.status_code >= 400:
#                         st.error(f"❌ Error: {res.data}")
#                     else:
#                         st.success("✅ Content updated successfully!")
#         else:
#             st.info("No records found.")
#     except Exception as e:
#         st.error(f"❌ Error: {e}")
#
# # ---------- DELETE ----------
# with tabs[3]:
#     st.header("Delete Content")
#     try:
#         response = supabase.table("Feed").select("*").execute()
#         records = response.data
#         search_term = st.text_input("🔍 Search by producer name", key="delete_search")
#
#         if search_term:
#             records = [r for r in records if search_term.lower() in r["producer_name"].lower()]
#
#         producers = [f"{r['producer_name']} - {r['title']}" for r in records]
#         selected_display = st.selectbox("Select content to delete", producers, key="delete_selectbox")
#         selected_record = next((r for r in records if f"{r['producer_name']} - {r['title']}" == selected_display), None)
#
#         if st.button("Delete", key="delete_button"):
#             res = supabase.table("Feed").delete().eq("id", selected_record["id"]).execute()
#             if res.status_code >= 400:
#                 st.error(f"❌ Error: {res.data}")
#             else:
#                 st.success("🗑️ Deleted successfully!")
#     except Exception as e:
#         st.error(f"❌ Error: {e}")
#
# # ---------- USERS TAB ----------
# with tabs[4]:
#     st.header("Manage Authenticated Users")
#
#     user_tabs = st.tabs(["➕ Add User", "📋 List Users", "📝 Update User", "❌ Delete User"])
#
#     # 1. Add User
#     with user_tabs[0]:
#         st.subheader("Add New User")
#         new_email = st.text_input("Email", key="new_email")
#         new_full_name = st.text_input("Full Name", key="new_full_name")
#         new_password = st.text_input("Password", type="password", key="new_password")
#
#         if st.button("Create User", key="create_user_button"):
#             if not new_email or not new_password:
#                 st.error("Email and password are required!")
#             else:
#                 try:
#                     res = create_user(new_email, new_password)
#                     if res.get("id"):
#                         user_id = res["id"]
#                         insert_res = supabase.table("authenticated_users").insert({
#                             "id": user_id,
#                             "email": new_email,
#                             "full_name": new_full_name
#                         }).execute()
#                         if insert_res.status_code >= 400:
#                             st.warning(f"User created but failed to add profile: {insert_res.data}")
#                         else:
#                             st.success(f"User created with ID: {user_id}")
#                     else:
#                         st.error(f"Failed to create user: {res.get('error', res)}")
#                 except Exception as e:
#                     st.error(f"Exception: {e}")
#
#     # 2. List Users
#     with user_tabs[1]:
#         st.subheader("List Users")
#         try:
#             profiles_res = supabase.table("authenticated_users").select("*").execute()
#             profiles = profiles_res.data
#
#             if profiles:
#                 for p in profiles:
#                     st.markdown(f"**ID:** {p['id']}")
#                     st.markdown(f"**Email:** {p['email']}")
#                     st.markdown(f"**Full Name:** {p.get('full_name', '')}")
#                     st.markdown("---")
#             else:
#                 st.info("No users found.")
#         except Exception as e:
#             st.error(f"Error fetching users: {e}")
#
#     # 3. Update User
#     with user_tabs[2]:
#         st.subheader("Update User")
#
#         try:
#             profiles_res = supabase.table("authenticated_users").select("*").execute()
#             profiles = profiles_res.data
#
#             if profiles:
#                 user_display = [f"{p['email']} - {p.get('full_name', '')}" for p in profiles]
#                 selected_user = st.selectbox("Select user to update", user_display)
#
#                 user_obj = next((p for p in profiles if f"{p['email']} - {p.get('full_name', '')}" == selected_user), None)
#
#                 if user_obj:
#                     updated_email = st.text_input("Email", value=user_obj["email"], key="update_email")
#                     updated_full_name = st.text_input("Full Name", value=user_obj.get("full_name", ""), key="update_full_name")
#                     updated_password = st.text_input("New Password (leave blank to keep unchanged)", type="password", key="update_password")
#
#                     if st.button("Update User", key="update_user_button"):
#                         update_data = {
#                             "email": updated_email,
#                             "full_name": updated_full_name
#                         }
#                         try:
#                             update_auth_resp = update_user(user_obj["id"], email=updated_email, password=updated_password if updated_password else None)
#                             if update_auth_resp.get("id"):
#                                 update_profile_res = supabase.table("authenticated_users").update(update_data).eq("id", user_obj["id"]).execute()
#                                 if update_profile_res.status_code >= 400:
#                                     st.warning(f"User auth updated but profile update failed: {update_profile_res.data}")
#                                 else:
#                                     st.success("User updated successfully!")
#                             else:
#                                 st.error(f"Failed to update auth user: {update_auth_resp.get('error', update_auth_resp)}")
#                         except Exception as e:
#                             st.error(f"Exception during update: {e}")
#             else:
#                 st.info("No users found.")
#         except Exception as e:
#             st.error(f"Error fetching users: {e}")
#
#     # 4. Delete User
#     with user_tabs[3]:
#         st.subheader("Delete User")
#         try:
#             profiles_res = supabase.table("authenticated_users").select("*").execute()
#             profiles = profiles_res.data
#
#             if profiles:
#                 user_display = [f"{p['email']} - {p.get('full_name', '')}" for p in profiles]
#                 selected_user = st.selectbox("Select user to delete", user_display)
#
#                 user_obj = next((p for p in profiles if f"{p['email']} - {p.get('full_name', '')}" == selected_user), None)
#
#                 if st.button("Delete User", key="delete_user_button"):
#                     try:
#                         del_auth_resp = delete_user(user_obj["id"])
#                         if del_auth_resp == {}:  # delete returns empty dict on success
#                             del_profile_resp = supabase.table("authenticated_users").delete().eq("id", user_obj["id"]).execute()
#                             if del_profile_resp.status_code >= 400:
#                                 st.warning(f"Auth user deleted but profile delete failed: {del_profile_resp.data}")
#                             else:
#                                 st.success("User deleted successfully!")
#                         else:
#                             st.error(f"Failed to delete auth user: {del_auth_resp.get('error', del_auth_resp)}")
#                     except Exception as e:
#                         st.error(f"Exception during deletion: {e}")
#             else:
#                 st.info("No users found.")
#         except Exception as e:
#             st.error(f"Error fetching users: {e}")




# loginv2
import streamlit as st
from supabase import create_client
from datetime import datetime
import uuid
import requests

# Load from secrets
SUPABASE_URL = st.secrets["supabase"]["url"]
SERVICE_ROLE_KEY = st.secrets["supabase"]["service_role_key"]  # Must be service role key!
supabase = create_client(SUPABASE_URL, SERVICE_ROLE_KEY)

HEADERS = {
    "apikey": SERVICE_ROLE_KEY,
    "Authorization": f"Bearer {SERVICE_ROLE_KEY}",
    "Content-Type": "application/json",
}

# --- Admin API helper functions ---
def create_user(email, password):
    url = f"{SUPABASE_URL}/auth/v1/admin/users"
    payload = {
        "email": email,
        "password": password,
        "email_confirm": True
    }
    r = requests.post(url, json=payload, headers=HEADERS)
    return r.json()

def update_user(user_id, email=None, password=None):
    url = f"{SUPABASE_URL}/auth/v1/admin/users/{user_id}"
    payload = {}
    if email:
        payload["email"] = email
    if password:
        payload["password"] = password
    r = requests.put(url, json=payload, headers=HEADERS)
    return r.json()

def delete_user(user_id):
    url = f"{SUPABASE_URL}/auth/v1/admin/users/{user_id}"
    r = requests.delete(url, headers=HEADERS)
    return r.json()

# ----------- Streamlit UI -----------

st.title("📚 Admin Panel - Content Manager")

tabs = st.tabs(["➕ Create", "📖 Read", "📝 Update", "❌ Delete", "👤 Users"])

# ---------- CREATE ----------
with tabs[0]:
    st.header("Add New Content")

    producer_name = st.text_input("Producer Name")
    title = st.text_input("Title")
    description = st.text_area("Description")
    content_type = st.selectbox("Content Type", ["Article", "Course", "CA", "Bizcomp"], key="create_content_type")
    tags = st.text_input("Tags (comma separated)")
    date_tag = st.date_input("Date Tag")
    img_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

    if st.button("Submit"):
        if img_file:
            try:
                unique_filename = f"{uuid.uuid4()}_{img_file.name}"
                file_bytes = img_file.read()
                supabase.storage.from_("feed-img").upload(unique_filename, file_bytes)
                public_url = supabase.storage.from_("feed-img").get_public_url(unique_filename)
            except Exception as e:
                st.error(f"❌ Upload failed: {e}")
                st.stop()
        else:
            public_url = ""

        data = {
            "producer_name": producer_name,
            "title": title,
            "Description": description,
            "content_type": content_type,
            "tags": tags,
            "date_tag": str(date_tag),
            "img_link": public_url,
        }

        try:
            supabase.table("Feed").insert(data).execute()
            st.success("✅ Content added successfully!")
        except Exception as e:
            st.error(f"❌ Error: {e}")

# ---------- READ ----------
with tabs[1]:
    st.header("View All Content")
    search_term = st.text_input("🔍 Search by title or producer name", key="read_search")

    try:
        response = supabase.table("Feed").select("*").execute()
        records = response.data

        if search_term:
            records = [r for r in records if search_term.lower() in r["title"].lower() or search_term.lower() in r["producer_name"].lower()]

        if records:
            for record in records:
                st.subheader(record["title"])
                st.markdown(f"**Producer:** {record['producer_name']}")
                st.markdown(f"**Type:** {record['content_type']}")
                st.markdown(f"**Tags:** {record['tags']}")
                st.markdown(f"**Date:** {record['date_tag']}")
                st.markdown(f"**Description:** {record['Description']}")
                if record["img_link"]:
                    st.image(record["img_link"], width=300)
                st.markdown("---")
        else:
            st.info("No records found.")
    except Exception as e:
        st.error(f"❌ Error: {e}")

# ---------- UPDATE ----------
with tabs[2]:
    st.header("Update Existing Content")
    try:
        response = supabase.table("Feed").select("*").execute()
        records = response.data
        search_term = st.text_input("🔍 Search by producer name", key="update_search")

        if search_term:
            records = [r for r in records if search_term.lower() in r["producer_name"].lower()]

        producers = [f"{r['producer_name']} - {r['title']}" for r in records]
        if producers:
            selected_display = st.selectbox("Select content by producer", producers, key="update_selectbox")
            selected_record = next((r for r in records if f"{r['producer_name']} - {r['title']}" == selected_display), None)

            if selected_record:
                new_title = st.text_input("Title", selected_record["title"])
                new_description = st.text_area("Description", selected_record["Description"])
                new_tags = st.text_input("Tags", selected_record["tags"])
                new_date_tag = st.date_input("Date Tag", datetime.strptime(selected_record["date_tag"], "%Y-%m-%d"))
                new_type = st.selectbox("Content Type", ["Article", "Course", "CA", "Bizcomp"], index=["Article", "Course", "CA", "Bizcomp"].index(selected_record["content_type"]), key="update_type")
                new_img = st.file_uploader("New Image (optional)", key="update_img")

                if st.button("Update"):
                    update_data = {
                        "title": new_title,
                        "Description": new_description,
                        "tags": new_tags,
                        "date_tag": str(new_date_tag),
                        "content_type": new_type,
                    }

                    if new_img:
                        unique_filename = f"{uuid.uuid4()}_{new_img.name}"
                        file_bytes = new_img.read()
                        supabase.storage.from_("feed-img").upload(unique_filename, file_bytes)
                        public_url = supabase.storage.from_("feed-img").get_public_url(unique_filename)
                        update_data["img_link"] = public_url

                    supabase.table("Feed").update(update_data).eq("id", selected_record["id"]).execute()
                    st.success("✅ Content updated successfully!")
        else:
            st.info("No records found.")
    except Exception as e:
        st.error(f"❌ Error: {e}")

# ---------- DELETE ----------
with tabs[3]:
    st.header("Delete Content")
    try:
        response = supabase.table("Feed").select("*").execute()
        records = response.data
        search_term = st.text_input("🔍 Search by producer name", key="delete_search")

        if search_term:
            records = [r for r in records if search_term.lower() in r["producer_name"].lower()]

        producers = [f"{r['producer_name']} - {r['title']}" for r in records]
        selected_display = st.selectbox("Select content to delete", producers, key="delete_selectbox")
        selected_record = next((r for r in records if f"{r['producer_name']} - {r['title']}" == selected_display), None)

        if st.button("Delete"):
            supabase.table("Feed").delete().eq("id", selected_record["id"]).execute()
            st.success("🗑️ Deleted successfully!")
    except Exception as e:
        st.error(f"❌ Error: {e}")

# ---------- USERS TAB ----------
with tabs[4]:
    st.header("Manage Authenticated Users")

    user_tabs = st.tabs(["➕ Add User", "📋 List Users", "📝 Update User", "❌ Delete User"])

    # 1. Add User
    with user_tabs[0]:
        st.subheader("Add New User")
        new_email = st.text_input("Email", key="new_email")
        new_full_name = st.text_input("Full Name", key="new_full_name")
        new_password = st.text_input("Password", type="password", key="new_password")

        if st.button("Create User"):
            if not new_email or not new_password:
                st.error("Email and password are required!")
            else:
                try:
                    res = create_user(new_email, new_password)
                    if res.get("id"):
                        user_id = res["id"]
                        insert_res = supabase.table("authenticated_users").insert({
                            "id": user_id,
                            "email": new_email,
                            "full_name": new_full_name
                        }).execute()
                        if insert_res.error:
                            st.warning(f"User created but failed to add profile: {insert_res.error.message}")
                        else:
                            st.success(f"User created with ID: {user_id}")
                    else:
                        st.error(f"Failed to create user: {res}")
                except Exception as e:
                    st.error(f"Exception: {e}")

    # 2. List Users
    with user_tabs[1]:
        st.subheader("List Users")
        try:
            profiles_res = supabase.table("authenticated_users").select("*").execute()
            profiles = profiles_res.data

            if profiles:
                for p in profiles:
                    st.markdown(f"**ID:** {p['id']}")
                    st.markdown(f"**Email:** {p['email']}")
                    st.markdown(f"**Full Name:** {p.get('full_name', '')}")
                    st.markdown("---")
            else:
                st.info("No users found.")
        except Exception as e:
            st.error(f"Error fetching users: {e}")

    # 3. Update User
    with user_tabs[2]:
        st.subheader("Update User")

        try:
            profiles_res = supabase.table("authenticated_users").select("*").execute()
            profiles = profiles_res.data

            if profiles:
                user_display = [f"{p['email']} - {p.get('full_name', '')}" for p in profiles]
                selected_user = st.selectbox("Select user to update", user_display)

                user_obj = next((p for p in profiles if f"{p['email']} - {p.get('full_name', '')}" == selected_user), None)

                if user_obj:
                    updated_email = st.text_input("Email", value=user_obj["email"], key="update_email")
                    updated_full_name = st.text_input("Full Name", value=user_obj.get("full_name", ""), key="update_full_name")
                    updated_password = st.text_input("New Password (leave blank to keep unchanged)", type="password", key="update_password")

                    if st.button("Update User"):
                        update_data = {
                            "email": updated_email,
                            "full_name": updated_full_name
                        }
                        try:
                            update_auth_resp = update_user(user_obj["id"], email=updated_email, password=updated_password if updated_password else None)
                            if update_auth_resp.get("id"):
                                update_profile_res = supabase.table("authenticated_users").update(update_data).eq("id", user_obj["id"]).execute()
                                if update_profile_res.error:
                                    st.warning(f"User auth updated but profile update failed: {update_profile_res.error.message}")
                                else:
                                    st.success("User updated successfully!")
                            else:
                                st.error(f"Failed to update auth user: {update_auth_resp}")
                        except Exception as e:
                            st.error(f"Exception during update: {e}")
            else:
                st.info("No users found.")
        except Exception as e:
            st.error(f"Error fetching users: {e}")


    def delete_user(user_id):
        url = f"{SUPABASE_URL}/auth/v1/admin/users/{user_id}"

        response = requests.delete(url, headers=HEADERS)

        if response.status_code == 204:
            return {}  # ✅ Success: user deleted
        else:
            # ❌ Failure: try to extract error details
            try:
                return response.json()  # Supabase usually returns JSON errors
            except Exception:
                # If not JSON, return raw response info
                return {
                    "error": "Failed to parse error response",
                    "status_code": response.status_code,
                    "text": response.text
                }

