import tkinter as tk
import random

# Function to generate a random number
def roll_dice():
    number = random.randint(1, 6)  # Random number between 1 and 6
    label.config(text=f"Dice Roll: {number}")

# Create the main window
root = tk.Tk()
root.title("Ludo Board with 10 Boxes")

# Create a canvas
canvas = tk.Canvas(root, width=500, height=200, bg="white")
canvas.pack()

# Define box size and position
box_size = 50
padding = 10

# Draw 10 boxes in a row
for i in range(10):
    x1 = i * (box_size + padding)
    y1 = 50
    x2 = x1 + box_size
    y2 = y1 + box_size
    canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="lightblue", width=2)

# Create a button to roll the dice
button = tk.Button(root, text="Roll Dice", command=roll_dice, font=("Arial", 14))
button.pack(pady=10)

# Label to display the random number
label = tk.Label(root, text="Dice Roll: ", font=("Arial", 14))
label.pack()

# Run the Tkinter event loop
root.mainloop()
