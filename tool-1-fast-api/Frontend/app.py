import streamlit as st
import requests

st.title("My AI Chat App")

if "token" not in st.session_state:
    st.session_state.token = None

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    response = requests.post(
        "http://localhost:8000/login",
        json={"email": email, "password": password}
    )
    if response.status_code == 200:
        st.session_state.token = response.json()["access_token"]
        st.success("Logged in!")
    else:
        st.error("Login failed")

if st.button("Get My Info"):
    headers = {"Authorization": f"Bearer {st.session_state.token}"}
    response = requests.get("http://localhost:8000/me", headers=headers)
    st.write(response.json())