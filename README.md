TalentScout – AI Hiring Assistant Chatbot

An intelligent AI-powered Hiring Assistant designed for screening technical candidates.
Built using Streamlit, Gradio, Python, and Large Language Models, TalentScout collects candidate information, analyzes tech stacks, and generates custom technical interview questions.

 Features
 1. Smart Candidate Information Collection

The chatbot gathers:

Full Name

Email

Phone Number

Experience

Desired Position

Current Location

Tech Stack (Languages, Frameworks, Tools)
 2. Tech-Stack–Based Question Generation
Example:
If candidate inputs Python + Django, the bot generates:

Python questions

Django framework questions

3. Natural Conversational Flow
Maintains context

Fallback responses for unclear messages

Graceful exit when user types: bye, exit, quit, thank you, stop
 4. Multiple UI Versions

app.py → Streamlit version

app_gradio.py → Gradio version

5. Secure & Privacy-Friendly

Candidate data handled only in memory

No storage of sensitive information

GDPR-aware simulated data use

🛠 Tech Stack
Component	Technology
UI	Streamlit, Gradio
Backend	Python
LLM	GPT-4o-mini / OpenAI API
Prompts	Custom Prompt Engineering
Deployment	Local / Streamlit Cloud
Project Structure
talentscout-hiring-assistant/
│── app.py                     # Streamlit version
│── app_gradio.py             # Gradio version
│── requirements.txt
│── README.md
│── prompts/
│     ├── system_prompt.txt
│     └── tech_question_prompt.txt
│── utils/
│── data/
│── demo/
│── assets/

 Installation & Setup
1️ Clone the Repository
git clone https://github.com/YOUR-USERNAME/talentscout-hiring-assistant.git
cd talentscout-hiring-assistant

2️ Install Dependencies
pip install -r requirements.txt

3️ Add Your OpenAI API Key
Option A — Streamlit Cloud (recommended)

Use:

Settings → Secrets → OPENAI_API_KEY="your_key"

Option B — Local .env File

Create .env:

OPENAI_API_KEY=your_key_here

 Running the App
Run Streamlit version
streamlit run app.py

Run Gradio version
python app_gradio.py

 Prompt Engineering Details
system_prompt.txt

Sets the bot’s identity

Defines conversation flow

Enforces professional recruiter tone

Provides info-collection sequence

tech_question_prompt.txt

Generates 3–5 technical questions

Tailored to candidate’s tech stack

Ensures difficulty level is appropriate

 Demo Video (Optional)

A Loom or YouTube walkthrough showing:

Chat flow

Tech stack entry

Question generation

Exit behavior

Upload inside /demo/ folder.

Testing Checklist

Bot greets user
Collects all required info
Detects tech stack
Generates relevant technical questions
Handles unclear inputs
Ends conversation gracefully
Works on Streamlit + Gradio
No sensitive data is stored

Enhancements
Advanced Features:
Sentiment analysis
Multilingual support
Personalized recommendations
Resume upload + parsing (future)

UI Improvements:
Custom CSS
Branding (TalentScout theme)
Progress indicators

 About This Project
This project was built as part of an AI/ML Internship assignment to demonstrate:
LLM integration
Prompt engineering
UI development
Context handling
Data privacy best practices

 Contact
For queries or suggestions:
shahalmuhammed9048@gamil.com