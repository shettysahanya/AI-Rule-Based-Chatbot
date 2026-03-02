import re

print("AI Chatbot started. Type 'exit' to quit.")

while True:
    user_input = input("You: ").lower()

    if re.search(r"\b(hi|hello|hey|namaste)\b", user_input):
        print("Chatbot: Hello! 😊")
    
    elif re.search(r"\bhow are you\b", user_input):
        
        print("Chatbot: I am great,how can i help you?")
    
    elif re.search(r"\byour name\b", user_input):
        print("Chatbot: I am an AI Rule-Based Chatbot.")
    
    elif user_input in ["exit", "bye"]:
        print("Chatbot: Goodbye see you later! 👋")
        break
    
    else:
        print("Chatbot: I don't understand that.")