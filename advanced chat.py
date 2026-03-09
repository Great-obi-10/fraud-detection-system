import random
import re

print("🤖 Advanced Rule-Based Chatbot")
print("Type 'exit' to stop the chat\n")


# -------------------------
# Knowledge base (responses)
# -------------------------

responses = {

    "greeting": [
        "Hello! 👋",
        "Hi there!",
        "Hey! How can I help you today?",
        "Nice to meet you!"
    ],

    "how_are_you": [
        "I'm doing great! Thanks for asking 😊",
        "I'm fine. How about you?",
        "All good here!"
    ],

    "ai": [
        "AI means Artificial Intelligence — machines that simulate human intelligence.",
        "Artificial Intelligence allows computers to learn from data.",
        "AI powers systems like chatbots, recommendation engines and self-driving cars."
    ],

    "nlp": [
        "NLP stands for Natural Language Processing.",
        "NLP helps computers understand human language.",
        "Examples include sentiment analysis, translation and chatbots."
    ],

    "sentiment": [
        "Sentiment analysis detects emotions in text.",
        "It classifies text as positive, negative or neutral.",
        "It is commonly used to analyze tweets and reviews."
    ],

    "goodbye": [
        "Goodbye! 👋",
        "See you later!",
        "Have a great day!"
    ],

    "unknown": [
        "I'm not sure I understand.",
        "Can you rephrase that?",
        "Interesting... tell me more."
    ]
}


# -------------------------
# Intent keywords
# -------------------------

intents = {

    "greeting": ["hello", "hi", "hey"],
    "how_are_you": ["how are you"],
    "ai": ["ai", "artificial intelligence"],
    "nlp": ["nlp", "natural language processing"],
    "sentiment": ["sentiment", "emotion", "feeling"]
}


# -------------------------
# Text preprocessing
# -------------------------

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text


# -------------------------
# Intent detection
# -------------------------

def detect_intent(user_input):

    for intent, keywords in intents.items():
        for word in keywords:
            if word in user_input:
                return intent

    return "unknown"


# -------------------------
# Chat loop
# -------------------------

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot:", random.choice(responses["goodbye"]))
        break

    clean_text = preprocess(user_input)

    intent = detect_intent(clean_text)

    reply = random.choice(responses[intent])

    print("Bot:", reply)