import tkinter as tk
from tkinter import messagebox

def show_info(event):
    messagebox.showinfo("Information", "This is some information.")

def hide_info(event):
    messagebox.showinfo("Information", "Information closed.")

# Create the main application window
app = tk.Tk()
app.title("Tkinter Info Label Example")

# Create a label with text and bind the <Enter> and <Leave> events
info_label = tk.Label(app, text="Hover over me for info", font=("Arial", 12), cursor="question_arrow")
info_label.pack(pady=20)
info_label.bind("<Enter>", show_info)
info_label.bind("<Leave>", hide_info)

# Run the Tkinter event loop
app.mainloop()
