import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Page settings
st.set_page_config(page_title="TalentScout AI Hiring Assistant", page_icon="🤖")
st.title("🤖 TalentScout – AI Hiring Assistant")
st.write("I will collect your details and generate technical questions based on your tech stack.")

# Load system prompt
def load_prompt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

system_prompt = load_prompt("prompts/system_prompt.txt")

# Session state for chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    try:
        full_prompt = f"{system_prompt}\n\nUser: {user_input}"

        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(full_prompt)

        reply = response.text

    except Exception as e:
        reply = f"Error: {e}"

    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)
