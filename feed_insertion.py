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
import streamlit as st
from supabase import create_client
import datetime

# Supabase client
url = st.secrets["supabase"]["url"]
key = st.secrets["supabase"]["key"]
supabase = create_client(url, key)

# Streamlit layout
st.set_page_config(page_title="Feed Admin Panel", layout="wide")
st.title("📦 Feed Admin Panel")

# Tabs for CRUD
tab1, tab2, tab3, tab4 = st.tabs(["➕ Create", "📄 Read", "✏️ Update", "❌ Delete"])

# CREATE
with tab1:
    st.subheader("Add New Feed Entry")

    producer_name = st.text_input("Producer Name")
    img_link = st.text_input("Image Link")
    title = st.text_input("Title")
    description = st.text_area("Description")
    content_type = st.selectbox("Content Type", ["Article", "Course", "CA", "BIzcomp"])
    tags = st.text_input("Tags (comma separated)")
    date_tag = st.date_input("Date Tag")

    if st.button("Create Entry"):
        data = {
            "producer_name": producer_name,
            "img_link": img_link,
            "title": title,
            "Description": description,
            "content_type": content_type,
            "tags": tags,
            "date_tag": date_tag.isoformat(),
        }
        try:
            supabase.table("Feed").insert(data).execute()
            st.success("✅ Successfully added!")
        except Exception as e:
            st.error(f"❌ Error: {e}")

# READ
with tab2:
    st.subheader("All Feed Entries")
    try:
        res = supabase.table("Feed").select("*").order("created_at", desc=True).execute()
        rows = res.data
        if rows:
            st.dataframe(rows)
        else:
            st.info("No entries found.")
    except Exception as e:
        st.error(f"❌ Error: {e}")

# UPDATE
with tab3:
    st.subheader("Update an Entry")

    try:
        entries = supabase.table("Feed").select("id, title").execute().data
        entry_dict = {f"{e['title']} ({e['id']})": e["id"] for e in entries}

        selected = st.selectbox("Select entry to update", list(entry_dict.keys()))
        if selected:
            entry_id = entry_dict[selected]
            full_entry = supabase.table("Feed").select("*").eq("id", entry_id).single().execute().data

            # Editable fields
            new_producer_name = st.text_input("Producer Name", full_entry["producer_name"])
            new_img_link = st.text_input("Image Link", full_entry["img_link"])
            new_title = st.text_input("Title", full_entry["title"])
            new_description = st.text_area("Description", full_entry.get("Description", ""))
            new_content_type = st.selectbox("Content Type", ["Article", "Course", "CA", "BIzcomp"], index=["Article", "Course", "CA", "BIzcomp"].index(full_entry["content_type"]))
            new_tags = st.text_input("Tags", full_entry["tags"])
            new_date_tag = st.date_input("Date Tag", datetime.date.fromisoformat(full_entry["date_tag"]))

            if st.button("Update Entry"):
                update_data = {
                    "producer_name": new_producer_name,
                    "img_link": new_img_link,
                    "title": new_title,
                    "Description": new_description,
                    "content_type": new_content_type,
                    "tags": new_tags,
                    "date_tag": new_date_tag.isoformat()
                }

                supabase.table("Feed").update(update_data).eq("id", entry_id).execute()
                st.success("✅ Entry updated!")

    except Exception as e:
        st.error(f"❌ Error: {e}")

# DELETE
with tab4:
    st.subheader("Delete an Entry")
    try:
        entries = supabase.table("Feed").select("id, title").execute().data
        entry_dict = {f"{e['title']} ({e['id']})": e["id"] for e in entries}

        selected = st.selectbox("Select entry to delete", list(entry_dict.keys()), key="delete_select")
        if selected:
            entry_id = entry_dict[selected]
            if st.button("Delete Entry", type="primary"):
                supabase.table("Feed").delete().eq("id", entry_id).execute()
                st.success("✅ Entry deleted.")
    except Exception as e:
        st.error(f"❌ Error: {e}")
