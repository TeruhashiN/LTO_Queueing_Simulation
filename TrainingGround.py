import tkinter as tk
from tkinter import messagebox


class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20

        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")

        label = tk.Label(self.tooltip, text=self.text, background="#ffffe0", relief="solid", borderwidth=1)
        label.pack(ipadx=1)

    def hide_tooltip(self, event):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

def show_info():
    messagebox.showinfo("Information", "This is some information.")

# Create the main application window
app = tk.Tk()
app.title("Tkinter Info Button Example")

# Create a label with the text "Info" and add a tooltip
info_label = tk.Label(app, text="?", font=("Arial", 12), cursor="question_arrow")
info_label.pack(pady=20)

# Associate the label with the tooltip
ToolTip(info_label, "Click for information")

# Bind the label to show_info function on click
info_label.bind("<Button-1>", lambda event: show_info())

# Run the Tkinter event loop
app.mainloop()
