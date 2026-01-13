# import gradio as gr
# import openai
# import os

# # ----------------------------
# # Load prompt files
# # ----------------------------
# def load_prompt(path):
#     with open(path, "r", encoding="utf-8") as f:
#         return f.read()

# SYSTEM_PROMPT = load_prompt("prompts/system_prompt.txt")
# TECH_QUESTION_PROMPT = load_prompt("prompts/tech_question_prompt.txt")

# # ----------------------------
# # LLM API
# # ----------------------------
# openai.api_key = os.getenv("OPENAI_API_KEY", "")

# def call_llm(messages):
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-4o-mini",
#             messages=messages,
#             temperature=0.4
#         )
#         return response.choices[0].message["content"]
#     except Exception as e:
#         return f"⚠️ Error: {str(e)}"

# # ----------------------------
# # Core Chatbot Function
# # ----------------------------
# def chatbot(user_message, history):

#     if history is None:
#         history = []

#     # Add user message to history
#     history.append(("user", user_message))

#     # Check exit keywords
#     exit_words = ["bye", "exit", "quit", "thank you", "stop"]
#     if any(word in user_message.lower() for word in exit_words):
#         bot_reply = "Thank you for interacting! TalentScout will reach out with next steps."
#         history.append(("assistant", bot_reply))
#         return history, history

#     # Check if user provided tech stack
#     tech_words = ["python", "java", "javascript", "sql", "react", "django", "node", "ml", "ai"]
#     if any(word in user_message.lower() for word in tech_words):
#         bot_reply = "Got it! I recorded your tech stack. Say **generate questions** to continue."
#         history.append(("assistant", bot_reply))
#         return history, history

#     # Generate technical questions
#     if "generate" in user_message.lower():
#         # Extract last-mentioned tech stack
#         tech_stack = user_message
        
#         q_prompt = TECH_QUESTION_PROMPT.replace("{{TECH_STACK}}", tech_stack)

#         messages = [{"role": "system", "content": q_prompt}]
#         bot_reply = call_llm(messages)
#         history.append(("assistant", bot_reply))
#         return history, history

#     # Default conversation mode (context + system)
#     messages = [{"role": "system", "content": SYSTEM_PROMPT}]
#     for role, content in history:
#         messages.append({"role": role, "content": content})

#     bot_reply = call_llm(messages)
#     history.append(("assistant", bot_reply))

#     return history, history


# # ----------------------------
# # Gradio UI
# # ----------------------------
# with gr.Blocks(theme=gr.themes.Soft()) as demo:
#     gr.Markdown("## 🤖 TalentScout – AI Hiring Assistant (Gradio Version)")
#     gr.Markdown("Provide details and your tech stack; say **generate questions** to get technical interview questions.")

#     chatbot_ui = gr.Chatbot(label="TalentScout Chat")
#     user_input = gr.Textbox(placeholder="Type your message here...")
#     state = gr.State([])

#     user_input.submit(chatbot, [user_input, state], [chatbot_ui, state])
#     user_input.submit(lambda: "", None, user_input)

# # Launch app
# if __name__ == "__main__":
#     demo.launch()
