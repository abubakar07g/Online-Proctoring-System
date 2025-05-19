import threading
from io import BytesIO
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import cvzone
import numpy as np
import pymysql
import winsound
from cvzone.FaceMeshModule import FaceMeshDetector
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams

def face_recognition_thread():
    root = tk.Toplevel()  # Use Toplevel so main root window is not blocked
    root.geometry("800x600+0+0")
    messagebox.showinfo('You Are Under Surveillance', "Make yourself around the webcam")

    cap = cv2.VideoCapture(0)
    cap.set(4, 500)  # width
    cap.set(5, 800)  # height

    detector = FaceMeshDetector(maxFaces=1)
    sensitivity = 2
    count = 0

    # Create frame for video in Tkinter window
    frame1 = tk.Frame(root, width=200, height=600, bg='red')
    frame1.pack(side='left', fill='both', expand=True)
    label = tk.Label(frame1)
    label.pack()

    while True:
        success, img = cap.read()
        if not success:
            break

        imgText = np.zeros_like(img)
        frame, faces = detector.findFaceMesh(img, draw=False)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

        if faces:
            face = faces[0]
            pointLeft = face[145]
            pointRight = face[374]
            w, _ = detector.findDistance(pointLeft, pointRight)
            W = 6.3  # average face width in cm
            f = 415  # focal length (calibrated)
            d = (W * f) / w  # distance in cm

            cvzone.putTextRect(img, f'Depth: {int(d)} cm', (face[10][0] - 100, face[10][1] - 50), scale=2)

            if d >= 80:
                count += 1
                frequency = 1000
                duration = 2000
                winsound.Beep(frequency, duration)

                if count == 1:
                    messagebox.showwarning("Warning", "First Warning: Your face is too far from the camera. Please move closer.")
                elif count == 2:
                    messagebox.showwarning("Warning", "Second Warning: Your face is too far from the camera. Please move closer.")
                elif count >= 3:
                    messagebox.showinfo("Warning", "Third Warning: You are eliminated.")
                    cap.release()
                    messagebox.showinfo('REPORT',
                                        "STUDENT NAME: ARVIND\nREG NO:21MIS0439\n"
                                        "YOU EXCEEDED THE LIMITATIONS.\n"
                                        "ALREADY WARNED TWO TIMES, NOW YOU ARE TERMINATED\n"
                                        "AND TREATED AS MALPRACTICE.\nWarning count = 3")
                    cv2.destroyAllWindows()
                    root.destroy()
                    break

        # Show instructional text
        textlist = ["All the best for ",
                    "your Examination",
                    "* Make sure you",
                    "have a reliable ",
                    "computer or ",
                    "laptop."]
        for i, text in enumerate(textlist):
            singleHeight = 20 + int((int(d / sensitivity) * sensitivity) / 4)
            cv2.putText(imgText, text, (50, 50 + (i * singleHeight)), cv2.FONT_ITALIC, 1, (255, 255, 255), 2)

        imgStacked = cvzone.stackImages([frame, imgText], 1, 1)
        cv2.imshow("Image", imgStacked)
        cv2.resizeWindow("Image", 355, 900)

    cap.release()
    cv2.destroyAllWindows()

def readfile_gui():
    connection = pymysql.connect(user='root', password='Abubakar@786',
                                 host='localhost', database='uploadfile')
    file_id = 4  # specify the file ID

    with connection.cursor() as cursor:
        sql = "SELECT contents FROM files WHERE id= %s"
        cursor.execute(sql, (file_id,))
        content = cursor.fetchone()[0]

    fp = BytesIO(content)
    laparams = LAParams()
    buffer = BytesIO()
    extract_text_to_fp(fp, buffer, laparams=laparams)
    text = buffer.getvalue().decode()

    root = tk.Toplevel()
    root.geometry("1000x900+0+0")

    frame2 = tk.Frame(root, width=1200, height=1000, bg='white', borderwidth=2, relief='solid')
    frame2.pack(side='right', fill='both', expand=True)

    text_widget = tk.Text(frame2, wrap='word', font=('Arial', 18, 'bold'))
    text_widget.pack(expand=True, fill='both')
    text_widget.insert('1.0', text)

    scrollbar_y = tk.Scrollbar(frame2, orient='vertical', command=text_widget.yview)
    scrollbar_y.pack(side='right', fill='y')
    text_widget.config(yscrollcommand=scrollbar_y.set)

    scrollbar_x = tk.Scrollbar(frame2, orient='horizontal', command=text_widget.xview)
    scrollbar_x.pack(side='bottom', fill='x')
    text_widget.config(xscrollcommand=scrollbar_x.set)

def student11():
    if checkbutton_var.get() == 1:
        # Start face recognition and file read in separate threads properly
        t1 = threading.Thread(target=face_recognition_thread)
        t2 = threading.Thread(target=readfile_gui)
        t1.start()
        t2.start()
    else:
        messagebox.showinfo('Warning', 'Please read and agree to the Terms & Conditions before proceeding.')

# Main GUI setup
root = tk.Tk()
root.title("Student Page")

# Background image
image = Image.open('forgetback.png')
background_image = ImageTk.PhotoImage(image)
background_label = tk.Label(root, image=background_image)
background_label.pack(fill=tk.BOTH, expand=True)

# VIT logo
bg1image = ImageTk.PhotoImage(file='vellore-institute-of-technology-vit-logo-vector-2022-xs.png')
vitlogo = tk.Label(root, image=bg1image)
vitlogo.place(x=85, y=20)

title_label = tk.Label(root, text="Student Page", fg="black", font=("Arial", 26), bd=2)
title_label.place(x=485, y=70)

info_text = (
    "->If the distance reading\n"
    "exceeds 80cm three times,\n"
    "you will be terminated,\n"
    "so be mindful of your \n"
    "distance from the camera."
)
termsconditions = tk.Label(root, text=info_text, bg='white', fg="black", font=("Arial", 13, 'bold'), bd=2)
termsconditions.place(x=455, y=180)

button1 = tk.Button(background_label, text="Start Exam", bg="lightblue", fg="black", font=("Arial", 14),
                    padx=10, pady=5, bd=2, relief=tk.GROOVE, command=student11)
button1.place(x=520, y=350)

checkbutton_var = tk.IntVar()
termsandcond = tk.Checkbutton(background_label, text='I agree to the Terms & Conditions',
                              font=('Microsoft Yahei UI Light', 10, 'bold'), fg='firebrick1', bg='white',
                              activebackground='white', activeforeground='firebrick1', cursor='hand2',
                              variable=checkbutton_var)
termsandcond.place(x=470, y=300)

root.mainloop()
