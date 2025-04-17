import tkinter as tk
from tkinter import colorchooser

# Initialize main window
root = tk.Tk()
root.title("My Paint App")
root.geometry("800x600")

# Global variables
current_color = "black"
brush_size = 5

# Canvas for drawing
canvas = tk.Canvas(root, bg="white", cursor="cross")
canvas.pack(fill=tk.BOTH, expand=True)

# Draw function
def draw(event):
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    canvas.create_oval(x1, y1, x2, y2, fill=current_color, outline=current_color)

canvas.bind("<B1-Motion>", draw)

# Color picker
def choose_color():
    global current_color
    color = colorchooser.askcolor()[1]
    if color:
        current_color = color

# Clear canvas
def clear_canvas():
    canvas.delete("all")

# UI controls
control_frame = tk.Frame(root, padx=5, pady=5)
control_frame.pack(side=tk.TOP, fill=tk.X)

color_button = tk.Button(control_frame, text="Pick Color", command=choose_color)
color_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(control_frame, text="Clear", command=clear_canvas)
clear_button.pack(side=tk.LEFT, padx=5)

# Run app
root.mainloop()
