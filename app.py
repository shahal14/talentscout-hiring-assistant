import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load env variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

# Page config
st.set_page_config(page_title="TalentScout AI Hiring Assistant", page_icon="🤖")
st.title("🤖 TalentScout – AI Hiring Assistant")
st.write("I will collect your details and generate technical questions based on your tech stack.")

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Load prompt
def load_prompt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

SYSTEM_PROMPT = load_prompt("prompts/system_prompt.txt")

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    try:
        chat = model.start_chat(history=[])
        response = chat.send_message(SYSTEM_PROMPT + "\nUser: " + user_input)
        reply = response.text
    except Exception as e:
        reply = f"Error: {e}"

    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)

