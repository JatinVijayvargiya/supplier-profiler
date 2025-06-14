import streamlit as st
import requests
import os

st.set_page_config(page_title="Supplier Profiler", layout="wide")

st.title("🔍 Supplier Profiler")
st.markdown("Enter the name of a supplier to fetch a summary of their business profile.")

query = st.text_input("Enter Supplier Name")

if st.button("Search") and query:
    api_key = st.secrets["454e94cadde871df054cb9492b4cd2d4f23ecb4b5078730896e29605f1198562"]
    params = {
        "engine": "google",
        "q": query,
        "api_key": api_key
    }
    response = requests.get("https://serpapi.com/search", params=params)
    if response.status_code == 200:
        results = response.json()
        if "organic_results" in results:
            for r in results["organic_results"][:3]:
                st.subheader(r.get("title"))
                st.write(r.get("snippet"))
                st.markdown(f"[🔗 Link]({r.get('link')})")
        else:
            st.warning("No results found.")
    else:
        st.error("Failed to fetch results. Check API key or usage limits.")