import tkinter as tk
from tkinter import filedialog, messagebox, font
from tkinter import scrolledtext, simpledialog

# Main window setup
root = tk.Tk()
root.title("Tkinter Notepad")
root.geometry("900x600")

# Default font settings
current_font_family = tk.StringVar(value="Arial")
current_font_size = tk.IntVar(value=12)
is_dark_mode = tk.BooleanVar(value=False)

# Text area
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, undo=True, font=(current_font_family.get(), current_font_size.get()))
text_area.pack(fill=tk.BOTH, expand=True)

# Function to update font
def update_font():
    new_font = (current_font_family.get(), current_font_size.get())
    text_area.configure(font=new_font)

# File operations
def new_file():
    if messagebox.askokcancel("New", "Start a new file?"):
        text_area.delete(1.0, tk.END)
        root.title("Untitled - Notepad")

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.INSERT, content)
            root.title(f"{file_path} - Notepad")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))
            root.title(f"{file_path} - Notepad")

def exit_app():
    if messagebox.askokcancel("Exit", "Do you really want to quit?"):
        root.destroy()

# Dark mode toggle
def toggle_dark_mode():
    if is_dark_mode.get():
        root.config(bg="#2e2e2e")
        text_area.config(bg="#1e1e1e", fg="white", insertbackground="white")
    else:
        root.config(bg="SystemButtonFace")
        text_area.config(bg="white", fg="black", insertbackground="black")

# Font selectors
def select_font_family():
    font_families = sorted(list(font.families()))
    choice = simpledialog.askstring("Font Family", "Choose font family:", initialvalue=current_font_family.get())
    if choice and choice in font_families:
        current_font_family.set(choice)
        update_font()
    elif choice:
        messagebox.showerror("Error", f"Font '{choice}' not found.")

def select_font_size():
    size = simpledialog.askinteger("Font Size", "Choose font size:", initialvalue=current_font_size.get(), minvalue=8, maxvalue=72)
    if size:
        current_font_size.set(size)
        update_font()

# Menu bar
menu_bar = tk.Menu(root)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open...", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

# View menu
view_menu = tk.Menu(menu_bar, tearoff=0)
view_menu.add_checkbutton(label="Dark Mode", variable=is_dark_mode, command=toggle_dark_mode)
menu_bar.add_cascade(label="View", menu=view_menu)

# Font menu
font_menu = tk.Menu(menu_bar, tearoff=0)
font_menu.add_command(label="Select Font Family", command=select_font_family)
font_menu.add_command(label="Select Font Size", command=select_font_size)
menu_bar.add_cascade(label="Font", menu=font_menu)

# Apply menu to root
root.config(menu=menu_bar)

# Initialize dark mode state
toggle_dark_mode()

# Shortcut key bindings
def select_all(event=None):
    text_area.tag_add("sel", "1.0", "end-1c")
    return "break"

# def copy_text(event=None):
#     text_area.event_generate("<<Copy>>")
#     return "break"

# def paste_text(event=None):
#     text_area.event_generate("<<Paste>>")
#     return "break"

root.bind("<Control-a>", select_all)
root.bind("<Control-A>", select_all)
# root.bind("<Control-c>", copy_text)
# root.bind("<Control-C>", copy_text)
# root.bind("<Control-v>", paste_text)
# root.bind("<Control-V>", paste_text)

# Run app
root.mainloop()
