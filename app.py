<<<<<<< HEAD
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
=======
import streamlit as st
import openai
import json
import os

# ----------------------------
#  LOAD PROMPTS
# ----------------------------
def load_prompt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

SYSTEM_PROMPT = load_prompt("prompts/system_prompt.txt")
TECH_QUESTION_PROMPT = load_prompt("prompts/tech_question_prompt.txt")


# ----------------------------
#  MODEL CALL
# ----------------------------
openai.api_key = st.secrets.get("OPENAI_API_KEY", "")

def call_llm(messages):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.4
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"[ERROR] {str(e)}"


# ----------------------------
#  INITIALIZE SESSION STATE
# ----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []
if "candidate_data" not in st.session_state:
    st.session_state.candidate_data = {
        "name": None,
        "email": None,
        "phone": None,
        "experience": None,
        "position": None,
        "location": None,
        "tech_stack": None,
        "questions_generated": False
    }


# ----------------------------
#  STREAMLIT UI
# ----------------------------
st.title("🤖 TalentScout - AI Hiring Assistant")
st.write("Welcome! This assistant will collect your details and generate technical questions based on your tech stack.")

# Chat container
chat_container = st.container()


with chat_container:
    # Display chat history
    for msg in st.session_state.messages:
        role = "user" if msg["role"] == "user" else "assistant"
        with st.chat_message(role):
            st.write(msg["content"])


# ----------------------------
#  USER INPUT
# ----------------------------
prompt = st.chat_input("Type your message here...")

if prompt:
    # Add user input to memory
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Conversation-ending keywords
    END_WORDS = ["bye", "thank you", "exit", "quit", "stop"]

    if any(word in prompt.lower() for word in END_WORDS):
        bot_reply = "Thank you for your time! The TalentScout hiring team will review your information and contact you soon."
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
        st.experimental_rerun()

    # ----------------------------
    #  CHECK IF TECH STACK PRESENT
    # ----------------------------
    candidate = st.session_state.candidate_data

    # Detect tech stack entry
    if candidate["tech_stack"] is None:
        if any(tech_word in prompt.lower() for tech_word in ["python","java","react","django","sql","node","ml","ai"]):
            candidate["tech_stack"] = prompt
            bot_reply = "Great! I’ve recorded your tech stack. Shall I generate relevant technical questions now?"
            st.session_state.messages.append({"role": "assistant", "content": bot_reply})
            st.experimental_rerun()

    # ----------------------------
    #  GENERATE TECHNICAL QUESTIONS
    # ----------------------------
    if "generate" in prompt.lower() and candidate["tech_stack"]:
        tech_prompt = TECH_QUESTION_PROMPT.replace("{{TECH_STACK}}", candidate["tech_stack"])
        
        messages = [
            {"role": "system", "content": tech_prompt}
        ]

        bot_reply = call_llm(messages)
        candidate["questions_generated"] = True

        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
        st.experimental_rerun()

    # ----------------------------
    # GENERIC LLM CHAT MODE
    # ----------------------------
    merged_messages = [{"role": "system", "content": SYSTEM_PROMPT}] + st.session_state.messages
    bot_reply = call_llm(merged_messages)

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    # Refresh page
    st.experimental_rerun()
>>>>>>> 35d6a7f (Convert app to Gemini API (free))
