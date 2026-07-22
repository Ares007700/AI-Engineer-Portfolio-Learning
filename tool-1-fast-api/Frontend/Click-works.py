import streamlit as st
import requests

st.title("My AI Chat App")

if st.button("Get Items"):
    response = requests.get("http://localhost:8000/items")
    st.write(response.json())