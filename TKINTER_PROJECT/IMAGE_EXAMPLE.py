import tkinter as tk
from PIL import Image, ImageTk  # pip install pillow

root = tk.Tk()
root.geometry("300x300")
root.title("Display PNG Image")

# Load image and resize
image = Image.open("pizza.png")
image = image.resize((150, 150))  # Set width and height (e.g., 300x300)
photo = ImageTk.PhotoImage(image)

# Display in a label
label = tk.Label(root, image=photo)
label.pack()

root.mainloop()
