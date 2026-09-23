# 🤖 Simple ChatBot

A lightweight **NLP-based chatbot** built with Python, spaCy, and Streamlit. It identifies basic conversational intents and generates responses from predefined response sets.

## ✨ Features

* Greeting detection
* Farewell detection
* Name-related queries
* Thank-you responses
* Basic conversational responses
* Randomized responses
* Interactive Streamlit interface

## 🧠 How It Works

```text
User Input
    │
    ▼
spaCy NLP Processing
    │
    ▼
Intent Detection
    │
    ▼
Predefined Response Selection
    │
    ▼
Chatbot Response
```

The application processes user input with **spaCy**, identifies supported conversational patterns, and selects an appropriate response from predefined responses.

## 🛠️ Tech Stack

**Python · spaCy · Streamlit**

## 🌐 Live Demo

**Try the ChatBot:**
https://projectchatbot-h5xdx2w7zvnsenepu4ecms.streamlit.app/

## 📁 Project Structure

```text
Project_chatbot/
├── chatbot.py
├── requirements.txt
├── README.md
└── output chatbot.jpeg
```

## 🚀 Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run chatbot.py
```

The application will open in your browser through Streamlit.

