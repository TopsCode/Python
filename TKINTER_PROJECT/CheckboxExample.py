import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Checkbox Example")

# Variable to store checkbox state
var = tk.IntVar()

# Function to display checkbox state
def show_state():
    print(f"Checkbox is {'Checked' if var.get() else 'Unchecked'}")

# Create a Checkbox
checkbox = tk.Checkbutton(root, text="Check Me", variable=var, command=show_state)
checkbox.pack(pady=10)

# Run the main loop
root.mainloop()
