import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Tkinter Buttons with Loop")

# Function to handle button click
def on_button_click(num):
    print(f"Button {num} clicked")

# Create buttons using a loop
for i in range(1, 7):
    btn = tk.Button(root, text=f"Button {i}", command=lambda i=i: on_button_click(i))
    btn.pack(pady=5)  # Add some spacing

# Run the Tkinter event loop
root.mainloop()
