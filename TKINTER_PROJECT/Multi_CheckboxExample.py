import tkinter as tk

root = tk.Tk()
root.title("Multiple Checkboxes")

# Variables for multiple checkboxes
var1 = tk.IntVar()
var2 = tk.IntVar()

# Function to show states
def show_states():
    print(f"Option 1: {'Checked' if var1.get() else 'Unchecked'}")
    print(f"Option 2: {'Checked' if var2.get() else 'Unchecked'}")

# Create checkboxes
cb1 = tk.Checkbutton(root, text="Option 1", variable=var1, command=show_states)
cb2 = tk.Checkbutton(root, text="Option 2", variable=var2, command=show_states)

cb1.pack(pady=5)
cb2.pack(pady=5)

root.mainloop()
