import tkinter as tk
from tkinter import StringVar

def update_list():
    selected_items.clear()
    for var, text in checkboxes:
        if var.get():
            selected_items.append(text)
    listbox.delete(0, tk.END)
    for item in selected_items:
        listbox.insert(tk.END, item)

# Create main window
root = tk.Tk()
root.title("Checkbox Example")

# List of options
options = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
checkboxes = []
selected_items = []

# Create checkboxes
tk.Label(root, text="Select Fruits:").pack(anchor=tk.W)
for option in options:
    var = tk.BooleanVar()
    chk = tk.Checkbutton(root, text=option, variable=var)
    chk.pack(anchor=tk.W)
    checkboxes.append((var, option))

# Button to update list
btn = tk.Button(root, text="Show Selected", command=update_list)
btn.pack()

# Listbox to display selected items
listbox = tk.Listbox(root)
listbox.pack()

root.mainloop()
