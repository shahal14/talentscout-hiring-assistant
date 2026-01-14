import streamlit as st
from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

# MUST be first Streamlit command
st.set_page_config(
    page_title="TalentScout AI Hiring Assistant",
    page_icon="🤖"
)

load_dotenv()
HF_TOKEN = os.getenv("HF_API_TOKEN")

# Router-compatible client (NEW SDK REQUIRED)
client = InferenceClient(
    token=HF_TOKEN
)

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
        prompt = f"""You are an AI hiring assistant.
Ask technical interview questions based on the candidate's tech stack.

User: {user_input}
Assistant:"""

        reply = client.text_generation(
            model="google/gemma-2b-it",  # ✅ GUARANTEED router model
            prompt=prompt,
            max_new_tokens=300,
            temperature=0.4
        )

    except Exception as e:
        reply = f"Error: {e}"

    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)
