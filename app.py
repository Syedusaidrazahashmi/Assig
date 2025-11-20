import streamlit as st
from api import get_all_assignments

st.set_page_config(page_title="Assignment Tracker", layout="wide")
st.title("📘 Assignment Tracker Dashboard")

assignments = get_all_assignments()

if len(assignments) == 0:
    st.info("No assignments found.")
else:
    st.dataframe(assignments, use_container_width=True)

st.markdown("### Navigation")
st.write("➡️ Use the left sidebar to add, edit, or view assignments.")
