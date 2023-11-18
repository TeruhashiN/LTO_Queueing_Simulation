from tkinter import Tk, Button, PhotoImage

def restart_program():
    print("Restarting the program")

def toggle_visibility():
    if restart_button.winfo_ismapped():
        restart_button.pack_forget()
    else:
        restart_button.pack()

# Create the main Tkinter window
root = Tk()
root.title("Restart Button Example")

# Load an image (replace 'path/to/your/image.png' with the actual path to your image file)
image_path = 'LTO Image/restart.png'
img = PhotoImage(file=image_path)

# Create a restart button with an image and set the size
restart_button = Button(root, text="Restart", image=img, command=restart_program, width=30, height=30)
restart_button.place(x=5, y=5)

# Create a button to toggle the visibility of the restart button
toggle_button = Button(root, text="Toggle Visibility", command=toggle_visibility)
toggle_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
