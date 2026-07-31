# AI Educational Assistant

An AI-powered educational chatbot built using **Python**, **Streamlit**, and **Google Gemini API**. The application provides interactive conversations on programming, Artificial Intelligence, Machine Learning, Data Structures, Algorithms, and Software Engineering through a clean and responsive interface.

This project was developed as part of the **EncoderX AI/ML Internship – Week 04 (AI Chatbot Development)**.

---

## Live Demo

**Application:** https://encoderx-chatbot-6zdf69o7zxen2hfyfsbnuk.streamlit.app/

---

## GitHub Repository

https://github.com/atif929/encoderx-chatbot

---

# Features

- AI-powered educational chatbot using Google Gemini
- Multi-chat conversation support
- Conversation history management
- Create, rename, and delete chat sessions
- Clean and responsive dark-mode interface
- Professional ChatGPT/Grok-inspired UI
- Suggested learning prompts
- Context-aware conversations
- Session-based chat management
- Secure API key management using environment variables

---

# Technologies Used

## Frontend

- Streamlit
- HTML
- CSS

## Backend

- Python
- Google Gemini API

## Libraries

- streamlit
- google-generativeai
- python-dotenv

---

# Project Structure

```
encoderx-ai-chatbot/
│
├── backend/
│   ├── chatbot.py
│   └── prompts.py
│
├── frontend/
│   ├── chat.py
│   ├── hero.py
│   ├── sidebar.py
│   └── cards.py
│
├── styles/
│   └── style.css
│
├── utils/
│   └── session.py
│
├── .streamlit/
│   └── config.toml
│
├── .env
├── .gitignore
├── app.py
├── requirements.txt
├── README.md
└── REPORT.md
```

---

# How It Works

1. User enters a question.
2. The application sends the query to the Google Gemini model.
3. Gemini generates a response using the provided system prompt.
4. The response is displayed in the chat interface.
5. Conversation history is maintained for contextual responses.

---

# Installation

## Clone the repository

```bash
git clone https://github.com/atif929/encoderx-chatbot.git
```

## Navigate into the project

```bash
cd encoderx-chatbot
```

## Create a virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY
```

You can generate an API key from **Google AI Studio**.

---

## Run the application

```bash
streamlit run app.py
```

---

# Screenshots

Add screenshots here after deployment.

### Landing Page

`images/home.png`

### Chat Interface

`images/chat.png`

### Sidebar

`images/sidebar.png`

---

# Future Improvements

- User authentication
- Voice conversations
- PDF document chat
- Image understanding
- File upload support
- Chat export
- Database integration
- Multiple AI model support
- Markdown rendering improvements

---

# Learning Outcomes

Through this project, I gained practical experience in:

- Large Language Models (LLMs)
- Prompt Engineering
- Google Gemini API Integration
- Streamlit Application Development
- Session State Management
- Responsive UI Design
- AI Application Deployment
- Environment Variable Management
- Git and GitHub Workflow

---

# Deployment

The application is deployed using **Streamlit Community Cloud**.

Deployment Link:

```
https://encoderx-chatbot-6zdf69o7zxen2hfyfsbnuk.streamlit.app/
```

---

# Author

**Atif Rameez**


GitHub: https://github.com/atif929

LinkedIn: https://www.linkedin.com/in/atif-rameez-b92ba7390/

---

# Internship Information

**Program:** EncoderX Remote Internship Program 01

**Track:** Artificial Intelligence / Machine Learning

**Week:** 04

**Task:** AI Chatbot Development

---

# License

This project is developed for educational and learning purposes as part of the EncoderX AI/ML Internship Program.