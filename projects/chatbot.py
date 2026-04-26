# Chatbot using dictionary and string operations

responses = {
    "hello": "Hello! How can I assist you today?",
    "how are you": "I'm doing well, thank you for asking!",
    "what is your name": "I am a simple chatbot.",
    "bye": "Goodbye! Have a great day!",
    "what can you do": "I can respond to simple greetings and questions. Try asking me something!",
    # Add 10 more.
}

print("Welcome to the chatbot! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower() # Hello -> hello
    if user_input == "bye":
        print("Chatbot: " + responses["bye"])
        break
    # Flag to track if a matching keyword was found
    matched = False
    for key, reply in responses.items():
        if key in user_input:
            print("Chatbot: " + reply)
            matched = True
            break
    if not matched:
        print("Chatbot: I'm sorry, I don't understand that.")