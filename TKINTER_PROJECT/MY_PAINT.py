import tkinter as tk
from tkinter import colorchooser, filedialog, ttk
from PIL import ImageGrab

# Initialize main window
root = tk.Tk()
root.title("🎨 My Paint App")
root.geometry("900x650")
root.configure(bg="#f0f0f0")

# Global variables
current_color = "#000000"
brush_size = 5
brush_shape = "round"
is_eraser = False
undo_stack = []

# Canvas for drawing
canvas = tk.Canvas(root, bg="white", cursor="cross", bd=2, relief=tk.RIDGE)
canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Draw function
def draw(event):
    global undo_stack
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    color = "white" if is_eraser else current_color
    
    if brush_shape == "round":
        shape = canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color)
    elif brush_shape == "square":
        shape = canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
    elif brush_shape == "line":
        shape = canvas.create_line(event.x, event.y, event.x + 1, event.y + 1,
                                   fill=color, width=brush_size * 2, capstyle=tk.ROUND)
    undo_stack.append(shape)

canvas.bind("<B1-Motion>", draw)

# Color picker
def choose_color():
    global current_color, is_eraser
    is_eraser = False
    color = colorchooser.askcolor()[1]
    if color:
        current_color = color
        color_button.config(bg=color)

# Clear canvas
def clear_canvas():
    global undo_stack
    canvas.delete("all")
    undo_stack = []

# Brush size update
def update_brush_size(value):
    global brush_size
    brush_size = int(float(value))
    brush_size_label.config(text=f"{brush_size}")

# Undo
def undo():
    if undo_stack:
        canvas.delete(undo_stack.pop())

# Brush shape update
def set_shape(shape):
    global brush_shape
    brush_shape = shape

# Eraser mode
def toggle_eraser():
    global is_eraser
    is_eraser = not is_eraser
    eraser_button.config(relief=tk.SUNKEN if is_eraser else tk.RAISED)

# Save canvas as image
def save_artwork():
    x = root.winfo_rootx() + canvas.winfo_x()
    y = root.winfo_rooty() + canvas.winfo_y()
    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()
    
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png")])
    if file_path:
        ImageGrab.grab().crop((x, y, x1, y1)).save(file_path)

# Title
title_label = tk.Label(root, text="🖌️ Welcome to My Paint App", font=("Helvetica", 20, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=10)

# UI controls
control_frame = tk.Frame(root, bg="#f0f0f0")
control_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

color_button = tk.Button(control_frame, text="🎨 Pick Color", command=choose_color, font=("Helvetica", 12),
                         bg=current_color, fg="white", width=12)
color_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(control_frame, text="🧹 Clear", command=clear_canvas, font=("Helvetica", 12),
                         bg="#e74c3c", fg="white", width=12)
clear_button.pack(side=tk.LEFT, padx=5)

undo_button = tk.Button(control_frame, text="↩️ Undo", command=undo, font=("Helvetica", 12),
                        bg="#3498db", fg="white", width=12)
undo_button.pack(side=tk.LEFT, padx=5)

save_button = tk.Button(control_frame, text="💾 Save", command=save_artwork, font=("Helvetica", 12),
                        bg="#2ecc71", fg="white", width=12)
save_button.pack(side=tk.LEFT, padx=5)

eraser_button = tk.Button(control_frame, text="🧽 Eraser", command=toggle_eraser, font=("Helvetica", 12),
                          bg="#9b59b6", fg="white", width=12)
eraser_button.pack(side=tk.LEFT, padx=5)

# Brush size and shape
brush_label = tk.Label(control_frame, text="🖍️  Brush Size", font=("Helvetica", 12), bg="#f0f0f0")
brush_label.pack(side=tk.LEFT, padx=10)

brush_slider = ttk.Scale(control_frame, from_=1, to=20, orient=tk.HORIZONTAL, command=update_brush_size)
brush_slider.set(5)
brush_slider.pack(side=tk.LEFT)

brush_size_label = tk.Label(control_frame, text=f"{brush_size}", font=("Helvetica", 12), bg="#f0f0f0")
brush_size_label.pack(side=tk.LEFT, padx=5)

# Brush shape buttons
shape_frame = tk.Frame(root, bg="#f0f0f0")
shape_frame.pack(pady=5)

tk.Label(shape_frame, text="✏️ Brush Shape:", font=("Helvetica", 12), bg="#f0f0f0").pack(side=tk.LEFT, padx=5)

shapes = [("Round", "round"), ("Square", "square"), ("Line", "line")]
for name, shape in shapes:
    b = tk.Button(shape_frame, text=name, command=lambda s=shape: set_shape(s),
                  font=("Helvetica", 11), bg="#bdc3c7", relief=tk.RAISED, width=8)
    b.pack(side=tk.LEFT, padx=3)

# Run app
root.mainloop()
