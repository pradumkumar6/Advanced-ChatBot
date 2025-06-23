# backend.py (updated with memory recall)
import os
from dotenv import load_dotenv
from euriai import EuriaiLangChainLLM
from langchain_core.messages import HumanMessage
from memory import store_message, fetch_session_history

# Load env variables
load_dotenv()

# Initialize Euriai LLM
llm = EuriaiLangChainLLM(
    api_key=os.getenv("EURIAI_API_KEY"),
    model="gpt-4.1-nano",  # Or any other supported model
    temperature=0.7,
    max_tokens=300
)

def generate_reply(session_id, user_message):
    history = fetch_session_history(session_id)
    messages = [
        HumanMessage(content="You are a friendly chatbot. Always try to remember the user's name, preferences, and prior conversations.")
    ]

    for msg, reply in history[-5:]:  # limit to last few interactions
        messages.append(HumanMessage(content=msg))
        messages.append(HumanMessage(content=reply))

    messages.append(HumanMessage(content=user_message))

    reply = llm.invoke(messages)
    store_message(session_id, user_message, reply)
    return reply

def get_history(session_id):
    return fetch_session_history(session_id)
