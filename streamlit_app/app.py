import streamlit as st
import requests

st.set_page_config(page_title="🔐 AIMA Role Manager", layout="centered")
st.title("🧠 AI Meta-Agent Role Manager")
st.markdown("Simulate different user personas and see how tasks are routed (or rejected) based on roles.")

api_url = "http://localhost:8000"

st.sidebar.header("🔐 Simulate Login")
role_options = {
    "Student": {"username": "user123", "password": "test"},
    "Admin": {"username": "admin001", "password": "admin"}
}
selected_role = st.sidebar.selectbox("Choose a Role to Simulate", list(role_options.keys()))
credentials = role_options[selected_role]

if st.sidebar.button("Login as " + selected_role):
    response = requests.post(f"{api_url}/token", data={
        "username": credentials["username"],
        "password": credentials["password"]
    })
    if response.status_code == 200:
        token = response.json()["access_token"]
        st.session_state["token"] = token
        st.session_state["username"] = credentials["username"]
        st.session_state["role"] = selected_role
        st.success(f"✅ Logged in as {selected_role}")
    else:
        st.error("❌ Login failed. Check credentials or server.")

if "token" in st.session_state:
    st.markdown(f"### 👋 Welcome, **{st.session_state['username']}** ({st.session_state['role']})")
    user_query = st.text_area("✍️ Enter your task prompt:", "Summarize and extract deadlines")

    if st.button("Run Task"):
        headers = {"Authorization": f"Bearer {st.session_state['token']}"}
        res = requests.post(f"{api_url}/run-task", headers=headers, json={"user_query": user_query})
        if res.status_code == 200:
            st.success("✅ Task Executed")
            st.json(res.json())
        else:
            st.error(f"❌ Error {res.status_code}")
            st.json(res.json())

    with st.expander("🔍 View Token"):
        st.code(st.session_state["token"])
else:
    st.info("Login from the sidebar to simulate a persona and run tasks.")