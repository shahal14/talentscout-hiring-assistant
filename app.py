import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="TalentScout AI Hiring Assistant", page_icon="🤖")
st.title("🤖 TalentScout – AI Hiring Assistant")
st.write("I will collect your details and generate technical questions based on your tech stack.")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

def load_prompt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

system_prompt = load_prompt("prompts/system_prompt.txt")

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Add user msg to session
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    try:
        # Build full conversation
        messages = [{"role": "system", "content": system_prompt}]
        messages.extend(st.session_state.messages)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        reply = response.choices[0].message["content"]

    except Exception as e:
        reply = f"Error: {e}"

    # Add assistant reply to history
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)
