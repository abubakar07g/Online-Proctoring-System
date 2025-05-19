import tkinter as tk
from tkinter import messagebox
import pymysql

def delete_row():
    selection = table.curselection()
    if len(selection) == 0:
        messagebox.showwarning("Warning", "Please select a user to delete")
        return
    
    index = int(selection[0])
    user_data = table.get(index)
    user_id = user_data[0]  # Assuming ID is the first element
    
    # Confirm deletion
    confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete user ID {user_id}?")
    if not confirm:
        return
    
    try:
        cursor.execute("DELETE FROM `data` WHERE `id` = %s", (user_id,))
        conn.commit()
        table.delete(index)
        messagebox.showinfo("Success", "User deleted successfully")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to delete user: {e}")

def update_table():
    table.delete(0, tk.END)
    try:
        cursor.execute("SELECT * FROM `data`")
        rows = cursor.fetchall()
        for row in rows:
            table.insert(tk.END, row)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch users: {e}")

# Connect to the database
try:
    conn = pymysql.connect(user='root', password='Abubakar@786', host='localhost', database='userdata')
    cursor = conn.cursor()
except Exception as e:
    print(f"Database connection failed: {e}")
    exit(1)

# Create the GUI
root = tk.Tk()
root.title("User Data")
root.geometry("800x400")

# Create frame with border
frame = tk.Frame(root, highlightbackground="red", highlightthickness=2)
frame.pack(fill=tk.BOTH, expand=True)

# Create scrollbar
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create listbox as table
table = tk.Listbox(frame, yscrollcommand=scrollbar.set, font=('Arial', 14))
table.pack(fill=tk.BOTH, expand=True)

# Configure scrollbar to work with listbox
scrollbar.config(command=table.yview)

# Delete button
delete_button = tk.Button(root, text="Delete", command=delete_row, bg='green', fg='white', font=('Arial', 15))
delete_button.pack(side=tk.BOTTOM, pady=10)

# Populate the listbox with data
update_table()

# Start the GUI event loop
root.mainloop()

# Close the database connection when GUI is closed
conn.close()
