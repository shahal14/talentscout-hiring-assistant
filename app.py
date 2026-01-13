import streamlit as st
from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()

# Load token
HF_TOKEN = st.secrets.get("HF_TOKEN") or os.getenv("HF_TOKEN")

# Initialize HF client
client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    token=HF_TOKEN
)

st.set_page_config(page_title="TalentScout AI Hiring Assistant", page_icon="🤖")
st.title("🤖 TalentScout – AI Hiring Assistant")
st.write("I will collect your details and generate technical questions based on your tech stack.")

# Session memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    try:
        prompt = f"""
You are an AI hiring assistant.
Ask technical questions based on candidate tech stack.

Conversation:
{user_input}
"""

        response = client.text_generation(
            prompt=f"<s>[INST] {prompt} [/INST]",
            max_new_tokens=300,
            temperature=0.4
        )

        reply = response.strip()

    except Exception as e:
        reply = f"Error: {e}"

    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)
