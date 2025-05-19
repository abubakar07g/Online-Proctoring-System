from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def clear():
    emailEntry.delete(0, END)
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmEntry.delete(0, END)
    check.set(0)

def connect_db():
    if (emailEntry.get() == '' or usernameEntry.get() == '' or
        passwordEntry.get() == '' or confirmEntry.get() == ''):
        messagebox.showerror('Error', 'All Fields Are Required')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error', 'Password Mismatch')
    elif check.get() == 0:
        messagebox.showerror('Error', 'Please Accept the Terms & Conditions')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='Abubakar@786')
            mycursor = con.cursor()
        except Exception as e:
            messagebox.showerror('Error', f'Database Connectivity Issue: {e}')
            return

        try:
            # Create database if it doesn't exist
            mycursor.execute('CREATE DATABASE IF NOT EXISTS userdata')
            mycursor.execute('USE userdata')

            # Create table if it doesn't exist
            mycursor.execute('''CREATE TABLE IF NOT EXISTS data(
                                id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
                                email VARCHAR(50),
                                username VARCHAR(100),
                                password VARCHAR(30))''')

            # Check if username already exists
            query = 'SELECT * FROM data WHERE username=%s'
            mycursor.execute(query, (usernameEntry.get(),))
            row = mycursor.fetchone()

            if row is not None:
                messagebox.showerror('Error', 'Username Already Exists')
            else:
                query = 'INSERT INTO data(email, username, password) VALUES(%s, %s, %s)'
                mycursor.execute(query, (emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
                con.commit()
                messagebox.showinfo('Success', 'Registration is successful')
                clear()
                registration_window.destroy()

            con.close()
        except Exception as e:
            messagebox.showerror('Error', f'Error occurred: {e}')
            con.close()

registration_window = Tk()
registration_window.title('Signup Page')
# registration_window.resizable(False, False)

# Load background image
background = ImageTk.PhotoImage(file='bgloginpage.png')
bgLabel = Label(registration_window, image=background)
bgLabel.grid()

# Frame for form
frame = Frame(registration_window, bg='white')
frame.place(x=554, y=100)

# Logo image
bg1image = ImageTk.PhotoImage(file='vellore-institute-of-technology-vitlogo-vector-2022-xs.png')
vitlogo = Label(registration_window, image=bg1image)
vitlogo.place(x=200, y=80)

# Heading label
heading = Label(frame, text='CREATE AN ACCOUNT', font=('Microsoft Yahei UI Light', 18, 'bold'),
                bg='white', fg='firebrick1')
heading.grid(row=0, column=0, padx=10, pady=10)

# Email
emailLabel = Label(frame, text='Email', font=('Microsoft Yahei UI Light', 10, 'bold'),
                   bg='white', fg='firebrick1')
emailLabel.grid(row=1, column=0, sticky='w', padx=25, pady=(10, 0))
emailEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'),
                   fg='white', bg='firebrick1')
emailEntry.grid(row=2, column=0, sticky='w', padx=25)

# Username
usernameLabel = Label(frame, text='Username', font=('Microsoft Yahei UI Light', 10, 'bold'),
                      bg='white', fg='firebrick1')
usernameLabel.grid(row=3, column=0, sticky='w', padx=25, pady=(10, 0))
usernameEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'),
                      fg='white', bg='firebrick1')
usernameEntry.grid(row=4, column=0, sticky='w', padx=25)

# Password
passwordLabel = Label(frame, text='Password', font=('Microsoft Yahei UI Light', 10, 'bold'),
                      bg='white', fg='firebrick1')
passwordLabel.grid(row=5, column=0, sticky='w', padx=25, pady=(10, 0))
passwordEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'),
                      fg='white', bg='firebrick1', show='*')
passwordEntry.grid(row=6, column=0, sticky='w', padx=25)

# Confirm Password
confirmLabel = Label(frame, text='Confirm Password', font=('Microsoft Yahei UI Light', 10, 'bold'),
                     bg='white', fg='firebrick1')
confirmLabel.grid(row=7, column=0, sticky='w', padx=25, pady=(10, 0))
confirmEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'),
                     fg='white', bg='firebrick1', show='*')
confirmEntry.grid(row=8, column=0, sticky='w', padx=25)

# Terms and Conditions Checkbox
check = IntVar()
termsandcond = Checkbutton(frame, text='I agree to the Terms & Conditions',
                           font=('Microsoft Yahei UI Light', 10, 'bold'),
                           fg='firebrick1', bg='white',
                           activebackground='white', activeforeground='firebrick1',
                           cursor='hand2', variable=check)
termsandcond.grid(row=9, column=0, pady=10, padx=15)

# Signup Button
signupButton = Button(frame, text='Signup', font=('Open Sans', 9, 'bold'),
                      bd=0, bg='firebrick1', fg='white',
                      activebackground='firebrick1', activeforeground='white',
                      width=17, command=connect_db)
signupButton.grid(row=10, column=0, pady=10)

registration_window.mainloop()
