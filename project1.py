# Rule-Based AI Chatbot
# Artificial Intelligence - Project 1
print("________________________________________")
print("      Welcome to Rule-Based AI Chatbot")
print("Type 'bye' to exit the chatbot.")
print("________________________________________")

# Dictionary containing chatbot responses
responses = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi! Nice to meet you.",
    "how are you": "I am fine. Thank you for asking!",
    "what is your name": "I am a Rule-Based AI Chatbot.",
    "who created you": "I was created as Project 1.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "what can you do": "I can answer simple predefined questions.",
    "thank you": "You're welcome!",
    "thanks": "Happy to help!"
}

# Infinite loop
while True:

    # Take user input
    user_input = input("\nYou: ")

    # Convert input to lowercase and remove extra spaces
    user_input = user_input.strip().lower()

    # Exit condition
    if user_input == "bye" or user_input == "exit" or user_input == "quit":
        print("Bot: Goodbye! Have a great day.")
        break

    # Print response if found, otherwise default message
    print("Bot:", responses.get(user_input,
          "Sorry, I don't understand that."))