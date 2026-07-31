# AI Educational Assistant

## EncoderX Remote Internship Program 01
### AI / ML Internship – Week 04
### Project Report

---

# Project Information

**Project Title:** AI Educational Assistant

**Intern:** Atif Rameez

**University:** Sukkur IBA University

**Program:** BS Software Engineering

**Internship:** EncoderX Remote Internship Program 01

**Task:** Week 04 – AI Chatbot Development

**Duration:** 1 Week

---

# Introduction

Artificial Intelligence has transformed the way people learn and access information. AI-powered chatbots have become valuable tools in education by providing instant, interactive, and personalized assistance.

The objective of this project was to develop an AI Educational Assistant capable of answering programming, Artificial Intelligence, Machine Learning, and Software Engineering related questions using Google's Gemini Large Language Model.

The chatbot was designed with a modern, professional user interface and supports multiple chat sessions, conversation history, and contextual responses.

---

# Project Objectives

The primary objectives of this project were:

- Develop an AI-powered educational chatbot.
- Integrate Google Gemini API for intelligent responses.
- Build a responsive and professional user interface.
- Maintain conversation history.
- Allow users to create and manage multiple chat sessions.
- Deploy the application online using Streamlit Cloud.

---

# Technologies Used

## Programming Language

- Python

## Frontend

- Streamlit
- HTML
- CSS

## Backend

- Google Gemini API
- Python

## Libraries

- Streamlit
- Google Generative AI
- Python Dotenv

## Development Tools

- Visual Studio Code
- Git
- GitHub
- Streamlit Community Cloud

---

# System Architecture

```
                User

                  │

                  ▼

      Streamlit User Interface

                  │

                  ▼

      Chat Management & Session State

                  │

                  ▼

        Google Gemini API

                  │

                  ▼

          AI Generated Response

                  │

                  ▼

      Streamlit Chat Interface
```

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
├── app.py
├── requirements.txt
├── README.md
└── REPORT.md
```

---

# Features

The chatbot includes the following features:

- AI-powered educational assistant
- Google Gemini integration
- Context-aware conversations
- Multi-chat support
- Conversation history
- Rename chat sessions
- Delete chat sessions
- Responsive interface
- Professional dark theme
- Suggested learning prompts
- Secure API key management

---

# Working of the System

The application follows the workflow below:

1. The user enters a question through the chat interface.

2. The application stores the conversation in session history.

3. The user's query is sent to the Google Gemini API.

4. Gemini processes the request using the predefined educational system prompt.

5. The AI generates a relevant response.

6. The response is displayed within the chat interface.

7. Both user and assistant messages are saved, allowing contextual conversations throughout the session.

---

# User Interface Design

The interface was designed with simplicity and usability in mind.

Design goals included:

- Clean layout
- Responsive design
- Professional appearance
- Dark mode
- Easy navigation
- Minimal distractions
- Consistent spacing
- Modern typography

The overall design was inspired by modern AI chat applications while maintaining an educational focus.

---

# Challenges Faced

During development, several technical challenges were encountered:

### API Integration

Configuring the Google Gemini API securely using environment variables.

### Deployment

Managing API secrets correctly during deployment on Streamlit Community Cloud.

### Session Management

Maintaining multiple chat sessions while preserving conversation history.

### Responsive Design

Creating a consistent interface across desktop and mobile devices.

### User Experience

Designing an intuitive and distraction-free interface for educational use.

---

# Testing

The chatbot was tested on multiple scenarios including:

- General greetings
- Programming questions
- Machine Learning concepts
- Artificial Intelligence topics
- Software Engineering discussions
- Long conversations
- Multiple chat sessions
- Chat renaming
- Chat deletion

The application successfully handled all tested scenarios.

---

# Results

The final application successfully achieved the intended objectives.

The chatbot is capable of:

- Understanding educational questions.
- Generating meaningful AI responses.
- Maintaining contextual conversations.
- Managing multiple chat sessions.
- Providing a responsive user experience.
- Operating successfully on Streamlit Cloud.

---

# Learning Outcomes

This project provided practical experience in:

- Large Language Models (LLMs)
- Prompt Engineering
- Google Gemini API Integration
- Streamlit Application Development
- Python Backend Development
- Session State Management
- User Interface Design
- Cloud Deployment
- Git and GitHub Workflow
- Environment Variable Management

---

# Future Improvements

The following features can further enhance the chatbot:

- User authentication
- Voice interaction
- PDF document question answering
- Image understanding
- Chat export
- User profiles
- Database integration
- Retrieval-Augmented Generation (RAG)
- Multiple AI model support
- Conversation search

---

# Conclusion

The AI Educational Assistant successfully demonstrates the integration of modern Large Language Models into an educational application. The project combines AI capabilities with a clean and responsive interface to create an interactive learning experience.

This internship project strengthened practical skills in AI integration, backend development, frontend design, cloud deployment, and software engineering best practices. It also provided valuable experience in building and deploying real-world AI applications suitable for educational use.

---

# References

- Google AI Studio
- Google Gemini API Documentation
- Streamlit Documentation
- Python Documentation

---

# Repository

GitHub Repository:

https://github.com/atif929/encoderx-chatbot

---

# Live Application

Deployment:

https://encoderx-chatbot-6zdf69o7zxen2hfyfsbnuk.streamlit.app/

---

# Author

**Atif Rameez**

BS Software Engineering

Sukkur IBA University

EncoderX AI/ML Internship – Week 04

2026