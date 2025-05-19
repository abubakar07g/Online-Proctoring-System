from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import ImageTk, Image
import pymysql

def forgetpass():
    def forget_pass():
        if userentry.get() == '' or newpass.get() == '' or confirmpass.get() == '':
            messagebox.showerror('Error', 'All Fields Are Required', parent=window)
        elif newpass.get() != confirmpass.get():
            messagebox.showerror('Error', 'Password Mismatch', parent=window)
        else:
            con = pymysql.connect(host='localhost', user='root', password='arvind', database='userdata')
            mycursor = con.cursor()
            query = 'select * from data where username=%s'
            mycursor.execute(query, (userentry.get(),))
            row = mycursor.fetchone()
            if row is None:
                messagebox.showerror('Error', 'Incorrect Username', parent=window)
            else:
                query = 'update data set password=%s where username=%s'
                mycursor.execute(query, (newpass.get(), userentry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Password is reset. Please login with new password.', parent=window)
                window.destroy()

    window = Toplevel()
    window.title('Reset Password')

    forgetImage = ImageTk.PhotoImage(file='backgroundforget.jpg')
    ForgetLabel = Label(window, image=forgetImage)
    ForgetLabel.image = forgetImage
    ForgetLabel.grid()

    vitlogo_img = ImageTk.PhotoImage(file='vellore-institute-of-technology-vit-logo-vector-2022-xs.png')
    vitlogo = Label(window, image=vitlogo_img)
    vitlogo.image = vitlogo_img
    vitlogo.place(x=90, y=20)

    Label(window, text='RESET PASSWORD', font=('Arial', 18, 'bold'), bg='white', fg='magenta2').place(x=480, y=60)

    Label(window, text='Username', font=('Arial', 12, 'bold'), bg='white', fg='orchid1').place(x=470, y=130)
    userentry = Entry(window, width=25, fg='magenta2', font=('Arial', 11, 'bold'), bd=0)
    userentry.place(x=470, y=160)
    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=180)

    Label(window, text='New Password', font=('Arial', 12, 'bold'), bg='white', fg='orchid1').place(x=470, y=210)
    newpass = Entry(window, width=25, fg='magenta2', font=('Arial', 11, 'bold'), bd=0)
    newpass.place(x=470, y=240)
    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=260)

    Label(window, text='Confirm Password', font=('Arial', 12, 'bold'), bg='white', fg='orchid1').place(x=470, y=290)
    confirmpass = Entry(window, width=25, fg='magenta2', font=('Arial', 11, 'bold'), bd=0)
    confirmpass.place(x=470, y=320)
    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=340)

    Button(window, text='Submit', font=('Open Sans', 16, 'bold'), fg='white', bg='magenta2',
           activeforeground='white', activebackground='magenta2', cursor='hand2', bd=0, width=19,
           command=forget_pass).place(x=470, y=390)

    window.mainloop()

def login_user():
    if usernameEntry.get() == '' or passwordEntry.get() == '' or combo.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='Abubakar@786')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Connection is not established. Try again.')
            return

        query = 'use userdata'
        mycursor.execute(query)
        query = 'select * from data where username=%s and password=%s'
        mycursor.execute(query, (usernameEntry.get(), passwordEntry.get()))
        row = mycursor.fetchone()

        if row is None:
            messagebox.showerror('Error', 'Invalid username or password')
        else:
            messagebox.showinfo('Welcome', 'Login Successful')
            login_window.destroy()
            if selected_option.get() == 'student':
                import student_page
            elif selected_option.get() == 'faculty':
                import faculty_page
            elif selected_option.get() == 'admin':
                import Admin

def username_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)

def password_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)

def hide():
    openeye.config(file='closeyeloginpage.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='openeyeloginpage.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

# GUI setup
login_window = Tk()
login_window.geometry('990x660+50+50')
login_window.resizable(False, False)
login_window.title('Login Page')

bgImage = ImageTk.PhotoImage(file='bgloginpage.png')
bgLabel = Label(login_window, image=bgImage)
bgLabel.image = bgImage
bgLabel.place(x=0, y=0)

logoImage = ImageTk.PhotoImage(file='vellore-institute-of-technology-vit-logo-vector-2022-xs.png')
vitlogo = Label(login_window, image=logoImage)
vitlogo.image = logoImage
vitlogo.place(x=200, y=80)

Label(login_window, text='USER LOGIN', font=('Microsoft Yahei UI Light', 23, 'bold'),
      bg='white', fg='firebrick1').place(x=605, y=120)

usernameEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='firebrick1')
usernameEntry.place(x=580, y=200)
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', username_enter)
Frame(login_window, width=250, height=2, bg='firebrick1').place(x=580, y=222)

passwordEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='firebrick1')
passwordEntry.place(x=580, y=260)
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', password_enter)
Frame(login_window, width=250, height=2, bg='firebrick1').place(x=580, y=282)

openeye = PhotoImage(file='openeyeloginpage.png')
eyeButton = Button(login_window, image=openeye, bd=0, bg='white', activebackground='white',
                   command=hide, cursor='hand2')
eyeButton.place(x=800, y=255)

forgetButton = Button(login_window, text='Forgot Password', bd=0, bg='white', activebackground='white',
                      cursor='hand2', font=('Microsoft Yahei UI Light', 9, 'bold'),
                      fg='firebrick1', activeforeground='firebrick1', command=forgetpass)
forgetButton.place(x=715, y=295)

loginButton = Button(login_window, text='Login', font=('Open Sans', 16, 'bold'), fg='white', bg='firebrick1',
                     activeforeground='white', activebackground='firebrick1',
                     cursor='hand2', bd=0, width=19, command=login_user)
loginButton.place(x=573, y=420)

# Dropdown for role selection
options = ['admin', 'student', 'faculty']
selected_option = StringVar()
selected_option.set('')

Label(login_window, text="Select an option:", font=('Open Sans', 16, 'bold'),
      fg='white', bg='firebrick1', cursor='hand2', bd=0, width=19).place(x=573, y=330)

combo = Combobox(login_window, values=options, textvariable=selected_option,
                 font=('Open Sans', 16, 'bold'), width=19)
combo.place(x=573, y=360)

login_window.mainloop()
