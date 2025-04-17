import tkinter as tk
import random

# Create the main window
root = tk.Tk()
root.title("Ludo Game")

# Create a canvas
canvas = tk.Canvas(root, width=600, height=300, bg="white")
canvas.pack()

# Define box properties
box_size = 50
padding = 10
start_x = 20  # Starting position of the first box
start_y = 50
boxes = []

# Draw 10 boxes in a row
for i in range(10):
    x1 = start_x + i * (box_size + padding)
    y1 = start_y
    x2 = x1 + box_size
    y2 = y1 + box_size
    box = canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="lightblue", width=2)
    boxes.append((x1, y1, x2, y2))  # Store box coordinates

# Create a game piece (circle) in the first box
piece_radius = 15
piece_x = boxes[0][0] + box_size // 2
piece_y = boxes[0][1] + box_size // 2
piece = canvas.create_oval(piece_x - piece_radius, piece_y - piece_radius,
                           piece_x + piece_radius, piece_y + piece_radius, fill="red")

# Track the current position of the piece
current_position = 0

# Function to move the piece
def roll_dice():
    global current_position
    dice_roll = random.randint(1, 6)  # Random number between 1 and 6
    new_position = current_position + dice_roll  # Calculate new position

    # Ensure the piece does not go beyond the last box
    if new_position >= len(boxes):
        new_position = len(boxes) - 1

    # Get new box coordinates
    x1, y1, x2, y2 = boxes[new_position]

    # Update piece position
    canvas.coords(piece, x1 + box_size // 2 - piece_radius, y1 + box_size // 2 - piece_radius,
                         x1 + box_size // 2 + piece_radius, y1 + box_size // 2 + piece_radius)

    # Update the current position
    current_position = new_position

    # Update the label to show dice roll
    label.config(text=f"Dice Roll: {dice_roll}")

# Create a button to roll the dice
button = tk.Button(root, text="Roll Dice", command=roll_dice, font=("Arial", 14))
button.pack(pady=10)

# Label to display the random number
label = tk.Label(root, text="Dice Roll: ", font=("Arial", 14))
label.pack()

# Run the Tkinter event loop
root.mainloop()
