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
import streamlit as st
from supabase import create_client
import datetime
import os

# Load Supabase credentials
url = st.secrets["supabase"]["url"]
key = st.secrets["supabase"]["key"]
supabase = create_client(url, key)

st.set_page_config(page_title="Admin Panel - Feed CRUD", layout="wide")

st.title("📡 Admin Panel - Feed CRUD")

tab1, tab2, tab3, tab4 = st.tabs(["➕ Add", "📄 Read", "✏️ Update", "❌ Delete"])

# Helper: Upload image to Supabase Storage
def upload_image(file):
    try:
        path = f"feed/{file.name}"
        supabase.storage.from_("feed-img").upload(path, file)
        url = supabase.storage.from_("feed-img").get_public_url(path)
        return url
    except Exception as e:
        st.error(f"❌ Upload failed: {e}")
        return None

# ➕ Add
with tab1:
    st.subheader("Add New Feed Entry")
    with st.form("add_form"):
        producer_name = st.text_input("Producer Name")
        image_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
        title = st.text_input("Title")
        description = st.text_area("Description")
        content_type = st.selectbox("Content Type", ["Article", "Course", "CA", "BIzcomp"], key="add_content_type")
        tags = st.text_input("Tags (comma separated)")
        date_tag = st.date_input("Date Tag", datetime.date.today())
        submitted = st.form_submit_button("Submit")

        if submitted:
            if image_file:
                img_link = upload_image(image_file)
                if not img_link:
                    st.stop()
            else:
                st.error("Please upload an image.")
                st.stop()

            data = {
                "producer_name": producer_name,
                "img_link": img_link,
                "title": title,
                "Description": description,
                "content_type": content_type,
                "tags": tags,
                "date_tag": str(date_tag),
            }

            try:
                supabase.table("Feed").insert(data).execute()
                st.success("✅ Successfully added to Supabase!")
            except Exception as e:
                st.error(f"❌ Error uploading: {e}")

# 📄 Read
with tab2:
    st.subheader("All Feed Entries")
    search_term = st.text_input("🔍 Search by Title", key="read_search")
    try:
        res = supabase.table("Feed").select("*").execute()
        entries = res.data
        if search_term:
            entries = [e for e in entries if search_term.lower() in e["title"].lower()]
        for entry in entries:
            st.write(entry)
    except Exception as e:
        st.error(f"❌ Error fetching data: {e}")

# ✏️ Update
with tab3:
    st.subheader("Update Feed Entry")
    search_update = st.text_input("🔍 Search by Title", key="update_search")
    try:
        res = supabase.table("Feed").select("*").execute()
        entries = res.data
        if search_update:
            entries = [e for e in entries if search_update.lower() in e["title"].lower()]
        titles = [e["title"] for e in entries]
        if titles:
            selected_title = st.selectbox("Select Entry", titles, key="update_title_select")
            selected_entry = next(e for e in entries if e["title"] == selected_title)

            with st.form("update_form"):
                new_title = st.text_input("Title", value=selected_entry["title"])
                new_description = st.text_area("Description", value=selected_entry.get("Description", ""))
                new_content_type = st.selectbox("Content Type", ["Article", "Course", "CA", "BIzcomp"], index=["Article", "Course", "CA", "BIzcomp"].index(selected_entry["content_type"]), key="update_content_type")
                new_tags = st.text_input("Tags", value=selected_entry["tags"])
                new_date_tag = st.date_input("Date", value=datetime.date.fromisoformat(selected_entry["date_tag"]))
                new_image_file = st.file_uploader("Upload New Image (optional)", type=["png", "jpg", "jpeg"])

                update_submit = st.form_submit_button("Update")

                if update_submit:
                    update_data = {
                        "title": new_title,
                        "Description": new_description,
                        "content_type": new_content_type,
                        "tags": new_tags,
                        "date_tag": str(new_date_tag),
                    }

                    if new_image_file:
                        new_img_link = upload_image(new_image_file)
                        if new_img_link:
                            update_data["img_link"] = new_img_link

                    try:
                        supabase.table("Feed").update(update_data).eq("id", selected_entry["id"]).execute()
                        st.success("✅ Updated successfully!")
                    except Exception as e:
                        st.error(f"❌ Error updating: {e}")
        else:
            st.info("No matching entries found.")
    except Exception as e:
        st.error(f"❌ Error loading entries: {e}")

# ❌ Delete
with tab4:
    st.subheader("Delete Feed Entry")
    search_delete = st.text_input("🔍 Search by Title", key="delete_search")
    try:
        res = supabase.table("Feed").select("*").execute()
        entries = res.data
        if search_delete:
            entries = [e for e in entries if search_delete.lower() in e["title"].lower()]
        titles = [e["title"] for e in entries]
        if titles:
            selected_title = st.selectbox("Select Entry", titles, key="delete_title_select")
            selected_entry = next(e for e in entries if e["title"] == selected_title)
            if st.button("Delete"):
                try:
                    supabase.table("Feed").delete().eq("id", selected_entry["id"]).execute()
                    st.success("✅ Deleted successfully!")
                except Exception as e:
                    st.error(f"❌ Error deleting: {e}")
        else:
            st.info("No matching entries found.")
    except Exception as e:
        st.error(f"❌ Error loading entries: {e}")

