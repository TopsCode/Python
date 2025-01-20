import tkinter as tk
from tkinter import filedialog, messagebox

# Initialize the main window
root = tk.Tk()
root.title("Notepad")

#######################  main logic #######################
# Function to open a file
def open_file():
    filepath = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if filepath:
        with open(filepath, 'r') as file:
            text_area.delete(1.0, tk.END)  # Clear the text area
            text_area.insert(tk.END, file.read())  # Insert file contents into text area
        root.title(f"Notepad - {filepath}")

# Function to save the current file
def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if filepath:
        with open(filepath, 'w') as file:
            file.write(text_area.get(1.0, tk.END))  # Get the text content and save to the file
        root.title(f"Notepad - {filepath}")

# Function to create a new file
def new_file():
    text_area.delete(1.0, tk.END)  # Clear the text area for a new file
    root.title("Notepad - New File")

# Function to exit the application
def exit_app():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

# Function to show About info
def show_about():
    messagebox.showinfo("About", "This App Created By - Anjali Patel")

# Create a Text widget for the editing area
text_area = tk.Text(root, wrap="word", undo=True)
text_area.pack(expand=True, fill=tk.BOTH)

# Create a menu bar
menu_bar = tk.Menu(root)

# Create the File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

# Create the About menu
about_menu = tk.Menu(menu_bar, tearoff=0)
about_menu.add_command(label="About", command=show_about)

# Add the File and About menus to the menu bar
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="About", menu=about_menu)

# Configure the main window to use the menu bar
root.config(menu=menu_bar)

# Run the Tkinter event loop
root.mainloop()
