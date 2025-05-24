# 🛡️ Online Proctoring System

A Python-based application designed to simulate a secure **online examination environment** using **face recognition**, **eye movement detection**, and **distance measurement** through a webcam. This system helps maintain academic integrity by continuously monitoring student behavior and issuing warnings or terminating the session upon suspicious activities.

---

## 🎯 Objective

To develop a real-time proctoring solution that:

- Ensures the student maintains proper eye contact with the webcam.
- Measures the distance between the student's eyes and the camera.
- Detects abnormal behaviors such as moving too far from the webcam or looking away repeatedly.
- Provides automated warnings and session termination to deter malpractice.

---

## 🔐 Key Features

- ✅ Role-based login (Admin / Faculty / Student)
- ✅ Registration and password recovery system
- 👨‍🏫 **Faculty Panel**: Upload question papers in PDF format
- 👨‍🎓 **Student Panel**:
  - Real-time webcam monitoring using OpenCV
  - Eye distance detection using FaceMesh
  - Eye movement tracking
  - Audible and visual warnings for violations
  - Termination on 3 consecutive violations
  - Display of question paper PDF within the app
- 🧑‍💼 **Admin Panel**: Add or remove users

---

## 🧰 Tech Stack

- **Language:** Python
- **GUI:** Tkinter
- **Webcam Processing:** OpenCV, cvzone
- **Face & Eye Detection:** FaceMeshDetector
- **Database:** MySQL with `pymysql`
- **File Handling:** pdfminer.six, easygui
- **Media & Alerts:** winsound, threading
- **Image Support:** PIL (Pillow)

---

## ⚙️ Setup Instructions

1. Install Required Dependencies
pip install opencv-python cvzone pymysql easygui pdfminer.six pillow

2. Set Up MySQL Databases
   
CREATE DATABASE userdata;
USE userdata;
CREATE TABLE data (
  id INT AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(50),
  username VARCHAR(100),
  password VARCHAR(30)
);

CREATE DATABASE uploadfile;
USE uploadfile;
CREATE TABLE files (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  contents LONGBLOB
);

3. Run the Application
python login.py

