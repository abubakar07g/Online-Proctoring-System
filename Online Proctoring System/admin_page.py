import tkinter as tk
from PIL import Image, ImageTk

# Functions for admin actions
def add_user():
    root.destroy()
    import add_user_page  # Make sure AddUser.py exists in the same directory

def delete_user():
    import delete_user_page  # Make sure Delete_User.py exists in the same directory

def logout():
    root.destroy()

# Initialize the main window
root = tk.Tk()
root.title("Admin Page")
root.geometry("990x660+50+50")
root.resizable(False, False)

# Load and display background image
image = Image.open('backgroundforget.jpg')
background_image = ImageTk.PhotoImage(image)
background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.grid()

# Load and display VIT logo
bg1image = ImageTk.PhotoImage(file='vellore-institute-of-technology-vit-logo-vector-2022-xs.png')
vitlogo_img = tk.Label(root, image=bg1image)
vitlogo_img.image = bg1image
vitlogo_img.place(x=85, y=20)

# Admin page heading
heading = tk.Label(root, text="  Admin Page  ", fg="black", font=("Arial", 26), bd=2, bg="white")
heading.place(x=480, y=70)

# Admin page buttons
button1 = tk.Button(background_label, text=" Add The Endusers ", bg="lightblue", fg="black",
                    font=("Arial", 14), padx=10, pady=5, bd=2, relief=tk.GROOVE, command=add_user)

button2 = tk.Button(background_label, text="Delete The Endusers", bg="lightgreen", fg="black",
                    font=("Arial", 14), padx=10, pady=5, bd=2, relief=tk.GROOVE, command=delete_user)

button3 = tk.Button(background_label, text=" Logout ", bg="lightpink", fg="black",
                    font=("Arial", 14), padx=10, pady=5, bd=2, relief=tk.GROOVE, command=logout)

# Place buttons on the window
button1.place(x=490, y=200)
button2.place(x=490, y=280)
button3.place(x=490, y=360)

# Start the main GUI loop
root.mainloop()
