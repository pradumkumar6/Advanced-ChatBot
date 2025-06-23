import streamlit as st
from backend import generate_reply

st.set_page_config(page_title="Euriai ChatBot", page_icon="🤖")
st.title("🧠 Euriai Chatbot with Memory")

# Session ID input
session_id = st.text_input("Enter your session ID (e.g. user123):", value="", max_chars=50)

# Get user message
user_input = st.chat_input("Type your message…")

# Display new message and response only (not all history)
if user_input and session_id:
    with st.chat_message("user"):
        st.write(user_input)

    reply = generate_reply(session_id, user_input)

    with st.chat_message("assistant"):
        st.write(reply)

# Optional: Show a friendly note if session is not set
elif not session_id:
    st.info("Please enter a session ID to start chatting.")
