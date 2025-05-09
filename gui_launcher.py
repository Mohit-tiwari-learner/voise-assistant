# gui_launcher.py

import tkinter as tk
from threading import Thread
import assistant

def start_assistant():
    Thread(target=assistant.run_assistant).start()

app = tk.Tk()
app.title("Voice Assistant")
app.geometry("300x200")

tk.Label(app, text="Voice Assistant", font=("Helvetica", 16)).pack(pady=20)
tk.Button(app, text="Start Listening", command=start_assistant, bg="green", fg="white").pack(pady=10)
tk.Button(app, text="Quit", command=app.quit, bg="red", fg="white").pack(pady=10)

app.mainloop()
