import tkinter as tk

# Create main window
root = tk.Tk()
root.geometry("300x300")
root.title("Tkinter Radiobutton Example")

# Variable to store selected value
selected_option = tk.StringVar(value="Option 1")  # Default value

# Function to display selected option
def show_selection():
    label.config(text=f"Selected: {selected_option.get()}")

# Create Radiobuttons
radio1 = tk.Radiobutton(root, text="Option 1", variable=selected_option, value="Option 1", command=show_selection)
radio2 = tk.Radiobutton(root, text="Option 2", variable=selected_option, value="Option 2", command=show_selection)
radio3 = tk.Radiobutton(root, text="Option 3", variable=selected_option, value="Option 3", command=show_selection)

# Pack Radiobuttons
radio1.pack(anchor="w")
radio2.pack(anchor="w")
radio3.pack(anchor="w")

# Label to display selected option
label = tk.Label(root, text="Selected: Option 1", font=("Arial", 12))
label.pack(pady=10)

# Run the main event loop
root.mainloop()
