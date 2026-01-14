import streamlit as st
from groq import Groq
import os

# MUST be first Streamlit call
st.set_page_config(
    page_title="TalentScout AI Hiring Assistant",
    page_icon="🤖"
)

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

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
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are an AI hiring assistant. Ask technical interview questions based on the candidate's tech stack."},
                *st.session_state.messages
                ],
            temperature=0.4,
            max_tokens=300
            )


        reply = completion.choices[0].message.content

    except Exception as e:
        reply = f"Error: {e}"

    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)
