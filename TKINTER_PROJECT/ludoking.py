import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("Ludo King")
root.geometry("600x600")

# Create a Canvas to draw the board
canvas = tk.Canvas(root, width=600, height=600, bg="white")
canvas.pack()

# Board Grid (15x15)
CELL_SIZE = 40  # Size of each cell
BOARD_SIZE = 15  # 15x15 grid

# Colors for player zones
player_colors = {"red": "#FF4C4C", "green": "#4CFF4C", "yellow": "#FFFF4C", "blue": "#4C4CFF"}

# Draw the board
def draw_board():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            x1, y1 = col * CELL_SIZE, row * CELL_SIZE
            x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE

            # Player home areas
            if row < 6 and col < 6:
                color = player_colors["red"]
            elif row < 6 and col > 8:
                color = player_colors["green"]
            elif row > 8 and col < 6:
                color = player_colors["yellow"]
            elif row > 8 and col > 8:
                color = player_colors["blue"]
            else:
                color = "white"

            # Draw the cell
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

    # Draw central winning area
    canvas.create_rectangle(6 * CELL_SIZE, 6 * CELL_SIZE, 9 * CELL_SIZE, 9 * CELL_SIZE, fill="white", outline="black")

    # Safe Zone paths (Gray)
    for i in range(6):
        # Vertical safe paths
        canvas.create_rectangle(7 * CELL_SIZE, i * CELL_SIZE, 8 * CELL_SIZE, (i + 1) * CELL_SIZE, fill="gray", outline="black")
        canvas.create_rectangle(7 * CELL_SIZE, (i + 9) * CELL_SIZE, 8 * CELL_SIZE, (i + 10) * CELL_SIZE, fill="gray", outline="black")

        # Horizontal safe paths
        canvas.create_rectangle(i * CELL_SIZE, 7 * CELL_SIZE, (i + 1) * CELL_SIZE, 8 * CELL_SIZE, fill="gray", outline="black")
        canvas.create_rectangle((i + 9) * CELL_SIZE, 7 * CELL_SIZE, (i + 10) * CELL_SIZE, 8 * CELL_SIZE, fill="gray", outline="black")

# Draw the board
draw_board()

# Run the Tkinter event loop
root.mainloop()
