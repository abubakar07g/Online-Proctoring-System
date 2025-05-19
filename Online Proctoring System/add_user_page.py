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
    if emailEntry.get() == '' or usernameEntry.get() == '' or passwordEntry.get() == '' or confirmEntry.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error', 'Password Mismatch')
    elif check.get() == 0:
        messagebox.showerror('Error', 'Please Accept the Terms & Conditions')
    else:
        # noinspection PyBroadException
        try:
            con = pymysql.connect(host='localhost', user='root', password='arvind')
            mycursor = con.cursor()

        except:
            messagebox.showerror('Error', 'Database Connectivity Issue, Please Try Again')
            return
        # noinspection PyBroadException
        try:
            query = 'create database userdata'
            mycursor.execute(query)
            query = 'use userdata'
            mycursor.execute(query)
            query = 'create table data(id int auto_increment primary key not null, email varchar(50),username ' \
                    'varchar(100),password varchar(30))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')

        query = 'select * from data where username=%s'
        mycursor.execute(query, (usernameEntry.get()))

        row = mycursor.fetchone()
        if row is not None:
            messagebox.showerror('Error', 'Username Already Exists')
        else:
            query = 'insert into data(email,username,password) values(%s,%s,%s)'
            mycursor.execute(query, (emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Registration is successful')
            clear()
            registration_window.destroy()


# def adduser():
#   registration_window.destroy()
#  import Admin


registration_window = Tk()
registration_window.title('Signup Page')
# registration_window.resizable(False, False)
background = ImageTk.PhotoImage(file='bgloginpage.png')

bgLabel = Label(registration_window, image=background)
bgLabel.grid()

frame = Frame(registration_window, bg='white')
frame.place(x=554, y=100)

bg1image = ImageTk.PhotoImage(file='vellore-institute-of-technology-vit-logo-vector-2022-xs.png')
vitlogo = Label(registration_window, image=bg1image)
vitlogo.place(x=200, y=80)

heading = Label(frame, text='CREATE AN ACCOUNT', font=('Microsoft Yahei UI Light', 18, 'bold')
                , bg='white', fg='firebrick1')
heading.grid(row=0, column=0, padx=10, pady=10)

emailLabel = Label(frame, text='Email', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white',
                   fg='firebrick1')
emailLabel.grid(row=1, column=0, sticky='w', padx=25, pady=(10, 0))

emailEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), fg='white', bg='firebrick1')
emailEntry.grid(row=2, column=0, sticky='w', padx=25)

usernameLabel = Label(frame, text='Username', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white',
                      fg='firebrick1')
usernameLabel.grid(row=3, column=0, sticky='w', padx=25, pady=(10, 0))

usernameEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), fg='white',
                      bg='firebrick1')
usernameEntry.grid(row=4, column=0, sticky='w', padx=25)

passwordLabel = Label(frame, text='Password', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white',
                      fg='firebrick1')
passwordLabel.grid(row=5, column=0, sticky='w', padx=25, pady=(10, 0))

passwordEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), fg='white',
                      bg='firebrick1')
passwordEntry.grid(row=6, column=0, sticky='w', padx=25)

confirmLabel = Label(frame, text='Confirm Password', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white',
                     fg='firebrick1')
confirmLabel.grid(row=7, column=0, sticky='w', padx=25, pady=(10, 0))

confirmEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), fg='white',
                     bg='firebrick1')
confirmEntry.grid(row=8, column=0, sticky='w', padx=25)

check = IntVar()
termsandcond = Checkbutton(frame, text='I agree to the Terms & Conditions',
                           font=('Microsoft Yahei UI Light', 10, 'bold'),
                           fg='firebrick1', bg='white', activebackground='white', activeforeground='firebrick1',
                           cursor='hand2', variable=check)
termsandcond.grid(row=9, column=0, pady=10, padx=15)

signupButton = Button(frame, text='Signup', font=('Open Sans', 9, 'bold'), bd=0, bg='firebrick1', fg='white',
                      activebackground='firebrick1', activeforeground='white', width=17, command=connect_db)
signupButton.grid(row=10, column=0, pady=10)

# button1 = Button(registration_window, text=" Back  ", bg="lightblue", fg="black", font=("Arial", 14), padx=10, pady=5,
#                bd=2, relief=GROOVE, command=adduser)
# Add the buttons to the window
# button1.place(x=10, y=10)

registration_window.mainloop()