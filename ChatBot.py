import tkinter as tk
from tkinter import scrolledtext
import re


class SmartChatbot:
    def __init__(self):
        self.context = ""
        self.responses = {
            'hello': 'Hello! How can I assist you today?',
            'how are you': 'I’m just a bot, but I’m doing great!',
            'bye': 'Goodbye! Have a great day!',
            'help': 'I can respond to "hello", "how are you", "bye", and more. Try asking me something else!',
            'what is your name': 'I am a chatbot created by Tharushi.',
            'default': 'Sorry, I don\'t understand that. Type "help" for assistance.',
            'what is your favorite color': 'I don\'t have a favorite color, but I can help you find out!',
            'what is your favorite movie': 'I don\'t have a favorite movie, but I can help you find out!'
        }

    def get_response(self, user_input):

        if 'weather' in user_input:
            return "I can't check the weather, but I can help with other queries!"
        if 'time' in user_input:
            from datetime import datetime
            return f"The current time is {datetime.now().strftime('%H:%M:%S')}."

        response = self.responses.get(user_input.lower(), self.responses['default'])
        return response

    def update_context(self, user_input):

        if 'hello' in user_input:
            self.context = 'greeting'
        elif 'bye' in user_input:
            self.context = 'farewell'
        else:
            self.context = ''


class ChatApp:
    def __init__(self, root, chatbot):
        self.chatbot = chatbot

        # Set up the chat window
        self.chat_window = scrolledtext.ScrolledText(root, width=80, height=20, state=tk.DISABLED)
        self.chat_window.pack()

        self.entry_box = tk.Entry(root, width=50)
        self.entry_box.pack()

        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack()

    def send_message(self):
        user_input = self.entry_box.get().strip().lower()

        if user_input:
            self.chat_window.config(state=tk.NORMAL)  # Enable editing to add new text
            self.chat_window.insert(tk.END, "You: " + user_input + '\n')

            self.chatbot.update_context(user_input)
            response = self.chatbot.get_response(user_input)
            self.chat_window.insert(tk.END, "Bot: " + response + '\n')

            self.entry_box.delete(0, tk.END)

            self.chat_window.yview(tk.END)
            self.chat_window.config(state=tk.DISABLED)

            if 'exit' in user_input:
                root.quit()
        else:
            self.chat_window.config(state=tk.NORMAL)
            self.chat_window.insert(tk.END, "Bot: Please type a message.\n")
            self.chat_window.config(state=tk.DISABLED)


root = tk.Tk()
root.title("Smart Chatbot")

chatbot = SmartChatbot()

app = ChatApp(root, chatbot)

root.mainloop()
