import streamlit as st
from backend import generate_reply, get_history
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Euriai Chatbot", page_icon="🤖", layout="centered")

st.markdown("""
    <style>
        body { background-color: #0E1117; color: #FAFAFA; }
        .stButton>button {
            background-color: #1f77b4;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 Euriai AI Chatbot")
session_id = st.text_input("Session ID", value="default_session")

if "messages" not in st.session_state:
    st.session_state.messages = get_history(session_id)

for msg, reply in st.session_state.messages:
    with st.chat_message("user"):
        st.markdown(msg)
    with st.chat_message("ai"):
        st.markdown(reply)

user_input = st.chat_input("Say something...")
if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)
    reply = generate_reply(session_id, user_input)
    with st.chat_message("ai"):
        st.markdown(reply)
    st.session_state.messages.append((user_input, reply))
