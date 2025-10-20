# TASK 4: Basic Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hi! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm fine, thanks for asking!"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day!"
    elif "your name" in user_input:
        return "I'm ChatBot 1.0 — your friendly assistant!"
    else:
        return "Sorry, I don't understand that."

print("ChatBot: Hello! Type 'bye' to end the chat.")
while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("ChatBot:", response)

    if "bye" in user_input.lower():
        break
