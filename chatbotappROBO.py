import tkinter as tk
from tkinter import simpledialog
import re
import random

def type_response(text, index=0):
    if index < len(text):
        chat_log.insert(tk.END, text[index], "bot")
        chat_log.after(30, type_response, text, index + 1)
    else:
        chat_log.insert(tk.END, "\n\n", "bot")
        chat_log.see(tk.END)

def send_message(event=None):
    user_input = entry.get().lower()

    if user_input.strip() == "":
        return

    chat_log.insert(tk.END, "You: " + user_input + "\n", "user")
    entry.delete(0, tk.END)

    if re.search(r"\b(hi|hello|hey|namaste)\b", user_input):
        response = f"Bot: Hello {name}! 😊"

    elif "how are you" in user_input:
        response = "Bot: I am great! How can I help you?"

    elif "your name" in user_input:
        response = "Bot: I am an AI Rule-Based Chatbot you can call me ROBO."

    elif "joke" in user_input:
        jokes = [
            "Bot: Why do programmers prefer dark mode? Because light attracts bugs! 😂",
            "Bot: Why did the computer show up at work late? It had a hard drive! 🤣",
            "Bot: Why do Java developers wear glasses? Because they don't C#! 😆"
        ]
        response = random.choice(jokes)

    elif user_input in ["bye", "exit"]:
        response = f"Bot: Goodbye {name}! 👋"

    else:
        response = "Bot: Sorry, I didn't understand that."

    type_response(response)


# Ask name popup
root = tk.Tk()
root.withdraw()

name = simpledialog.askstring("Name", "Greetings human 🤖 What is your name?")

# Main window
window = tk.Tk()
window.title("AI Chatbot")
window.geometry("420x500")
window.configure(bg="#ECE5DD")

# Chat area
chat_log = tk.Text(window, bg="#ECE5DD", font=("Arial", 11), wrap="word")
chat_log.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Message colors
chat_log.tag_config("user", foreground="blue")
chat_log.tag_config("bot", foreground="green")

# Welcome message
chat_log.insert(tk.END, f"Bot: Hello {name}! I am your AI assistant 🤖\n\n", "bot")
chat_log.insert(tk.END, "Bot: You can try asking things like:\n", "bot")
chat_log.insert(tk.END, "• Tell me a joke 😂\n", "bot")
chat_log.insert(tk.END, "• How are you?\n", "bot")
chat_log.insert(tk.END, "• What is your name?\n\n", "bot")

# Input area
frame = tk.Frame(window, bg="#ECE5DD")
frame.pack(pady=5)

entry = tk.Entry(frame, width=30, font=("Arial", 12))
entry.pack(side=tk.LEFT, padx=5)

entry.bind("<Return>", send_message)

send_button = tk.Button(frame, text="Send", command=send_message, bg="#25D366", fg="white")
send_button.pack(side=tk.LEFT)

window.mainloop()