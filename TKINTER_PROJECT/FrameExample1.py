import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Tkinter Button to Create Frame")

# Function to create a new frame on button click
def create_frame(num):
    frame = tk.Frame(root, bg="lightblue", width=200, height=100)
    frame.pack(pady=10)  # Add spacing
    label = tk.Label(frame, text=f"Frame {num}", bg="lightblue", font=("Arial", 12))
    label.pack(pady=10)  # Center label inside the frame

# Create buttons using a loop
for i in range(1, 7):
    btn = tk.Button(root, text=f"Button {i}", command=lambda i=i: create_frame(i))
    btn.pack(pady=5)  # Add spacing

# Run the Tkinter event loop
root.mainloop()
