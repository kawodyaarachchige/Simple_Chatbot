import tkinter as tk
from tkinter import scrolledtext

# Simple GUI Chatbot
def get_response(user_input):
    responses = {
        'hello': 'Hello! How can I assist you today?',
        'how are you': 'I’m just a bot, but I’m doing great!',
        'bye': 'Goodbye! Have a great day!',
    }
    return responses.get(user_input, "Sorry, I don't understand that.")

def send_message():
    user_input = entry_box.get().lower()
    chat_window.insert(tk.END, "You: " + user_input + '\n')

    response = get_response(user_input)
    chat_window.insert(tk.END, "Bot: " + response + '\n')

    entry_box.delete(0, tk.END)

    if 'bye' in user_input:
        root.quit()

# GUI Setup
root = tk.Tk()
root.title("Simple Chatbot")

chat_window = scrolledtext.ScrolledText(root, width=50, height=20)
chat_window.pack()

entry_box = tk.Entry(root, width=50)
entry_box.pack()

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

root.mainloop()
