import tkinter as tk

# Function to remove a widget and show a new frame
def switch_widget():
    widget_to_remove.place_forget()  # Remove the widget
    new_frame.place(x=50, y=100, width=300, height=150)  # Show new frame

# Initialize main window
root = tk.Tk()    
root.geometry("400x300")

# Widget to remove
widget_to_remove = tk.Label(root, text="This is a removable widget", font=("Arial", 14))
widget_to_remove.place(x=100, y=50)

# Button to trigger widget removal
remove_button = tk.Button(root, text="Remove Widget", command=switch_widget)
remove_button.place(x=150, y=200)

# New frame to display after widget removal
new_frame = tk.Frame(root, bg="lightblue")

# Adding content to the new frame
new_label = tk.Label(new_frame, text="This is the new frame!", font=("Arial", 14), bg="lightblue")
new_label.place(x=50, y=50)

# Run the application
root.mainloop()
