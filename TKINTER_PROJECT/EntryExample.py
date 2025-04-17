import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Tkinter Entry Example")

# Create an Entry widget
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Function to get input value
def get_text():
    user_input = entry.get()
    label.config(text=f"You entered: {user_input}")

# Create a button to fetch input
button = tk.Button(root, text="Get Input", command=get_text)
button.pack(pady=5)

# Label to display user input
label = tk.Label(root, text="Enter something above", font=("Arial", 12))
label.pack(pady=5)

# Run the main event loop
root.mainloop()
