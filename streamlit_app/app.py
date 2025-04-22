import streamlit as st
import requests

st.set_page_config(page_title="AIMA Role Manager", layout="centered")

st.title("🔐 AI Meta-Agent Role Manager")
st.markdown("Manage your access and run agentic tasks based on your user profile.")

api_url = "http://localhost:8000"

st.sidebar.header("Login")
username = st.sidebar.text_input("Username", value="user123")
password = st.sidebar.text_input("Password", type="password", value="test")

if st.sidebar.button("Login"):
    response = requests.post(f"{api_url}/token", data={"username": username, "password": password})
    if response.status_code == 200:
        token = response.json()["access_token"]
        st.session_state["token"] = token
        st.success("✅ Logged in successfully!")
    else:
        st.error("❌ Invalid credentials")

if "token" in st.session_state:
    st.markdown("### 🎯 Run a Task")
    user_query = st.text_area("Enter your task", value="Summarize and extract deadlines")

    if st.button("Run Task"):
        headers = {"Authorization": f"Bearer {st.session_state['token']}"}
        res = requests.post(f"{api_url}/run-task", headers=headers, json={"user_query": user_query})
        if res.status_code == 200:
            st.success("✅ Task Executed")
            st.json(res.json())
        else:
            st.error(f"❌ Error: {res.status_code}")
            st.json(res.json())

    with st.expander("🔍 View Token"):
        st.code(st.session_state["token"])
else:
    st.info("🔒 Please login first to run tasks.")