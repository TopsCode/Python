import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Background Color Changer")
root.geometry("300x200")

# Function to change background color
def change_bg():
    selected_color = color_var.get()
    root.configure(bg=selected_color)

# Variable to hold the selected radio button value
color_var = tk.StringVar(value="white")  # Default color

# Radio button options
colors = [("Red", "red"), ("Green", "green"), ("Blue", "blue"), ("Yellow", "yellow")]

# Creating radio buttons
for text, color in colors:
    radio = tk.Radiobutton(root, text=text, variable=color_var, value=color, command=change_bg)
    radio.pack(anchor="w", padx=20, pady=5)

root.mainloop()
