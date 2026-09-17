import streamlit as st
import spacy
import random

nlp = spacy.load("en_core_web_sm")

responses = {
    "greetings": ["Hello", "Hi there", "Hey! How can I help you?", "Greetings!", "Nice to see you!"],
    "farewell": ["Goodbye!", "See you soon!", "Bye! Have a great day", "Take care!", "Until next time"],
    "name_query": ["I'm ChatBot.", "You can call me ChatBot.", "I'm a simple ChatBot.", "My name is ChatBot."],
    "thanks": ["You are welcome", "No problem", "Anytime", "Glad to help", "You bet"],
    "how_are_you": ["I am just a program, but I am here to help!", "I am good, thanks for asking!", "I am here to assist you!", "Doing well, thanks!"],
    "default": ["I am not sure I understand", "Can you rephrase that", "I am here to help", "Sorry, I did not catch that", "Could you clarify that for me"]
}

def classify_input(user_input):
    doc = nlp(user_input.lower())

    if any(token.lemma_ in ["hello", "hi", "hey"] for token in doc):
        return "greetings"

    if any(token.lemma_ in ["bye", "goodbye", "later"] for token in doc):
        return "farewell"

    if "how" in [token.lemma_ for token in doc] and "you" in [token.lemma_ for token in doc]:
        return "how_are_you"

    if any(token.lemma_ in ["thanks", "thank"] for token in doc):
        return "thanks"

    if any(token.lemma_ == "name" for token in doc):
        return "name_query"

    return "default"

def generate_response(classification):
    return random.choice(responses[classification])

st.set_page_config(page_title="Simple ChatBot", page_icon="🤖")

st.title("🤖 Simple ChatBot")
st.write("A simple NLP chatbot built with Python and spaCy.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    classification = classify_input(user_input)
    response = generate_response(classification)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    st.rerun()
    
