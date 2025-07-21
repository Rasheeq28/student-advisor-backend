import streamlit as st
from supabase import create_client
import datetime

# Load from secrets
url = st.secrets["supabase"]["url"]
key = st.secrets["supabase"]["key"]

supabase = create_client(url, key)

st.title("Admin Panel - Content Uploader")

producer_name = st.text_input("Producer Name")
img_link = st.text_input("Image Link")
title = st.text_input("Title")
description = st.text_area("Description")
content_type = st.selectbox("Content Type", ["Article", "Course", "CA", "BIzcomp"])
tags = st.text_input("Tags (comma separated)")
date_tag = st.date_input("Date Tag")

if st.button("Submit"):
    data = {
        "producer_name": producer_name,
        "img_link": img_link,
        "title": title,
        "description": description,
        "content_type": content_type,
        "tags": tags,
        "date_tag": str(date_tag),
    }

    try:
        response = supabase.table("Feed").insert(data).execute()
        st.success("✅ Successfully added to Supabase!")
    except Exception as e:
        st.error(f"❌ Error: {e}")
