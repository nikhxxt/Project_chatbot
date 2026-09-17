import spacy
import random


nlp = spacy.load("en_core_web_sm")


responses = {
    "greetings": ["Hello","Hi there", "Hey! How can I help you?", "Greetings!", "Nice to see you!"],
    "farewell":  ["Goodbye!", "See you soon!", "Bye! Have a great day", "Take care!", "Untill next time"],
    "name_query": ["I'm ChatBot.", "You can call me ChatBot.", "I'm simple ChatBot.", "I can go by ChatBot.", "My name is ChatBot."],
    "name_provide": ["Nice to meet you, {name}!.", "Hello {name}.", "Great to meet you {name}.", "Pleased to meet you {name}.", "Hello there {name}.",],
    "thanks":  ["You are welcome", "No problem", "Anytime", "Glad to help", "You bet"],
    "how_are_you":  ["I am just a program,But i am here to help!", "I am good thanks for asking!", "I am here to assit you!", "Doing well, Thanks!", "I am okay, Thanks!",],
    "default": ["I am not sure I understand", "Can you rephrase that", "I am here to help", "Sorry i did not catch that", "Could you clarify that for me"]
}

                
def classify_input(user_input):
    doc = nlp(user_input.lower())
    for token in doc:
        if token.lemma_ in ["hello", "hi", "hey"]:
           return "greetings"
        elif token.lemma_ in ["bye", "goodbye", "later"]:
           return "farewell"
        elif token.lemma_ in ["name", "who"]:
           return "name_query"
        elif  token.lemma_ in ["thanks", "thank"]:
           return "thanks"
        elif  token.lemma_ in ["how", "hi", "hey"]:
              if any(t.lemma_ == "you" for t in doc):
                  return "how_are_you"
        elif  token.lemma_ in ["my", "i"]:
             if any(t.lemma_ == "name" for t in doc):
                return "name_provide"
    return "default"


def generate_response(classification, user_input=None):
    if classification == "name_provide":
       name = user_input.split()[-1]
       return random.choice(responses[classification]).format(name=name)
    return random.choice(responses[classification])
 
def chatbot():
    print("ChatBot: Hello!How can i assist you today?")
    while True:
        user_input = input("you: ")
        if user_input.lower() in ["exit", "quit", "bye", "goodbye"]:
           print("ChatBot: goodbye! Have a great day!")
           break
        classification = classify_input(user_input)
        response = generate_response(classification, user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
  chatbot()
        
    
