import streamlit as st
import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

# ----------------------------
# Hugging Face Client
# ----------------------------
client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    token=os.getenv("HF_API_TOKEN")
)

# ----------------------------
# Streamlit UI
# ----------------------------
st.set_page_config(page_title="TalentScout AI Hiring Assistant", page_icon="🤖")
st.title("🤖 TalentScout – AI Hiring Assistant")
st.write("I will collect your details and generate technical questions based on your tech stack.")

# Session memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    try:
        prompt = f"""
You are TalentScout, an AI hiring assistant.
Your task is to collect candidate details and generate technical interview questions
based on the candidate's tech stack.

User message:
{user_input}
"""

        response = client.text_generation(
            prompt=f"<s>[INST] {prompt} [/INST]",
            max_new_tokens=300,
            temperature=0.4,
            do_sample=True
        )

        reply = response.strip()

    except Exception as e:
        reply = f"Error: {e}"

    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)
