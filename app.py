import streamlit as st
from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_API_TOKEN")

client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    token=HF_TOKEN,
    base_url="https://router.huggingface.co"
)

st.set_page_config(page_title="TalentScout AI Hiring Assistant", page_icon="🤖")
st.title("🤖 TalentScout – AI Hiring Assistant")
st.write("I will collect your details and generate technical questions based on your tech stack.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    try:
        prompt = f"""
<s>[INST]
You are an AI hiring assistant.
Ask technical interview questions based on the candidate's tech stack.

User input:
{user_input}
[/INST]
"""

        reply = client.text_generation(
            prompt=prompt,
            max_new_tokens=300,
            temperature=0.4,
            do_sample=True
        )

    except Exception as e:
        reply = f"Error: {e}"

    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)
