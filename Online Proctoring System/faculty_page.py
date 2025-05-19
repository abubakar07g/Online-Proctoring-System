import cv2
import cvzone
import pymysql
import easygui
from tkinter import messagebox
import tkinter as tk
from PIL import Image, ImageTk

class Upload:
    def __init__(self):
        # Connect to MySQL database
        try:
            cnx = pymysql.connect(user='root', password='Abubakar@786',
                                  host='localhost', database='uploadfile')
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to connect to database: {e}")
            return

        messagebox.showinfo('Guidelines about file upload', "Make sure you upload a file in PDF format")

        # Select a file using easygui
        file_path = easygui.fileopenbox(filetypes=["*.pdf"])
        if not file_path:
            messagebox.showwarning("No File Selected", "No file was selected.")
            cnx.close()
            return

        # Read file contents
        try:
            with open(file_path, 'rb') as f:
                file_contents = f.read()
        except Exception as e:
            messagebox.showerror("File Error", f"Failed to read the file: {e}")
            cnx.close()
            return

        # Insert file contents into database
        try:
            cursor = cnx.cursor()
            query = "INSERT INTO files (name, contents) VALUES (%s, %s)"
            values = (file_path.split('/')[-1], file_contents)  # Save only file name
            cursor.execute(query, values)
            cnx.commit()
            messagebox.showinfo('Upload Status', "File Uploaded Successfully")
        except Exception as e:
            messagebox.showerror("Upload Error", f"Failed to upload file to database: {e}")
        finally:
            cursor.close()
            cnx.close()

def fileupload():
    if checkbutton_var.get() == 1:
        Upload()
    else:
        messagebox.showinfo('Warning', 'Please read and agree to the Terms & Conditions before proceeding.')

# Initialize main window
root = tk.Tk()
root.title("Faculty Page")
root.geometry("800x500")

# Load background image
try:
    image = Image.open('backgroundforget.jpg')
    background_image = ImageTk.PhotoImage(image)
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
except Exception as e:
    print(f"Background image load error: {e}")

# Load and place VIT logo
try:
    vitlogo_img = ImageTk.PhotoImage(file='vellore-institute-of-technology-vitlogo-vector-2022-xs.png')
    vitlogo = tk.Label(root, image=vitlogo_img, bg='white')
    vitlogo.place(x=90, y=20)
except Exception as e:
    print(f"Logo image load error: {e}")

# Title Label
title_label = tk.Label(root, text=" Faculty Page ", fg="black", font=("Arial", 26), bd=2, bg='white')
title_label.place(x=480, y=70)

# Instruction Label
instructions = '->> Make Sure You\n upload a Question,\n Bank must be in PDF\n Format'
termsconditions = tk.Label(root, text=instructions, bg='white', fg="black", font=("Arial", 13, 'bold'), bd=2)
termsconditions.place(x=455, y=180)

# Terms & Conditions Checkbox
checkbutton_var = tk.IntVar()
termsandcond = tk.Checkbutton(root, text='I agree to the Terms & Conditions',
                             font=('Microsoft Yahei UI Light', 10, 'bold'),
                             fg='firebrick1', bg='white',
                             activebackground='white', activeforeground='firebrick1',
                             cursor='hand2', variable=checkbutton_var)
termsandcond.place(x=470, y=270)

# Upload Button
upload_button = tk.Button(root, text=" Upload The Question Bank ",
                          bg="lightblue", fg="black", font=("Arial", 13),
                          padx=10, pady=5, bd=2, relief=tk.GROOVE, command=fileupload)
upload_button.place(x=480, y=370)

root.mainloop()
