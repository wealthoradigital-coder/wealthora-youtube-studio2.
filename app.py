import streamlit as st
import streamlit.components.v1 as components
import os

# 1. Page Configuration
st.set_page_config(page_title="Wealthora Studio Engine", layout="wide")

# 2. Safely read the HTML template file 
html_file_path = "studio.html"

if os.path.exists(html_file_path):
    with open(html_file_path, "r", encoding="utf-8") as f:
        wealthora_studio_html = f.read()
    
    # 3. Mount interface inside Streamlit container architecture
    components.html(wealthora_studio_html, height=1300, scrolling=True)
else:
    st.error(f"Missing interface component file! Please ensure '{html_file_path}' is uploaded to the repository directory.")
