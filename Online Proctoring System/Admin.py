import tkinter as tk
from PIL import Image, ImageTk


class Admin:
    def __init__(self):
        def add_user():
            root.destroy()
            import add_user_page
            Admin()

        def delete_user():
            import delete_user_page

        def logout():
            root.destroy()

        root = tk.Tk()

        # Set the title of the window
        root.title("Admin Page")

        # Define a function to execute when the buttons are clicked
        def button_click(button):
            print(f"You clicked {button['text']}")

        # Load the background image
        image = Image.open('backgroundforget.jpg')
        background_image = ImageTk.PhotoImage(image)

        # Create a label to hold the background image
        background_label = tk.Label(root, image=background_image)
        background_label.grid()

        bg1image = ImageTk.PhotoImage(file='vellore-institute-of-technology-vit-logo-vector-2022-xs.png')
        vitlogo = tk.Label(root, image=bg1image)
        vitlogo.place(x=85, y=20)

        vitlogo = tk.Label(root, text="  Admin Page  ", fg="black", font=("Arial", 26), bd=2)
        vitlogo.place(x=480, y=70)

        # Create the buttons
        button1 = tk.Button(background_label, text=" Add The Endusers   ", bg="lightblue", fg="black",
                            font=("Arial", 14),
                            padx=10, pady=5,
                            bd=2, relief=tk.GROOVE, command=add_user)
        button2 = tk.Button(background_label, text="Delete The Endusers", bg="lightgreen", fg="black",
                            font=("Arial", 14),
                            padx=10, pady=5,
                            bd=2, relief=tk.GROOVE, command=delete_user)
        button3 = tk.Button(background_label, text="            Logout             ", bg="lightpink", fg="black",
                            font=("Arial", 14), padx=10, pady=5,
                            bd=2, relief=tk.GROOVE, command=logout)

        # Add the buttons to the window
        button1.place(x=490, y=200)
        button2.place(x=490, y=280)
        button3.place(x=490, y=360)

        # Run the main event loop
        root.mainloop()