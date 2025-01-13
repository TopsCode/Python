import tkinter as tk

def on_button_click():
    label.config(text="Hello, Tkinter!")

window = tk.Tk()
window.title("Tkinter Example")
window.geometry("400x300")

label = tk.Label(window, text="Click the button", font=("Arial", 14))
label.pack(pady=20)

button = tk.Button(window, text="Click Me", command=on_button_click, font=("Arial", 14))
button.pack(pady=20)

window.mainloop()
