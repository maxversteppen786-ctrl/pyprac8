# Practical No. 8: Creating GUI Forms Using Tkinter
# Q.1: Create a Student Registration Form using Tkinter.
# File Name: student_registration.py

import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Student Registration Form")
root.geometry("500x500")
root.resizable(False, False)


# Q.1 (a): Function to submit the form
def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    course = course_entry.get()

    if name == "" or email == "" or course == "":
        messagebox.showwarning(
            "Warning",
            "Please fill all the fields."
        )
    else:
        messagebox.showinfo(
            "Registration Successful",
            "Name: " + name +
            "\nEmail: " + email +
            "\nCourse: " + course
        )


# Q.1 (b): Function to clear the form
def clear_form():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    text_box.delete("1.0", tk.END)


# Q.1 (c): Create menu bar
menubar = tk.Menu(root)

# File menu
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Clear", command=clear_form)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="File", menu=file_menu)

# Help menu
help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(
    label="About",
    command=lambda: messagebox.showinfo(
        "About",
        "Student Registration Form\nCreated using Python Tkinter"
    )
)
menubar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menubar)


# Q.1 (d): Create title label using pack()
title_label = tk.Label(
    root,
    text="Student Registration Form",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=15)


# Q.1 (e): Create form frame using pack()
form_frame = tk.Frame(root)
form_frame.pack(pady=10)


# Q.1 (f): Name label and text box using grid()
name_label = tk.Label(
    form_frame,
    text="Name:",
    font=("Arial", 12)
)
name_label.grid(
    row=0, column=0, padx=10, pady=10, sticky="w"
)

name_entry = tk.Entry(form_frame, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=10)


# Q.1 (g): Email label and text box using grid()
email_label = tk.Label(
    form_frame,
    text="Email:",
    font=("Arial", 12)
)
email_label.grid(
    row=1, column=0, padx=10, pady=10, sticky="w"
)

email_entry = tk.Entry(form_frame, width=30)
email_entry.grid(row=1, column=1, padx=10, pady=10)


# Q.1 (h): Course label and text box using grid()
course_label = tk.Label(
    form_frame,
    text="Course:",
    font=("Arial", 12)
)
course_label.grid(
    row=2, column=0, padx=10, pady=10, sticky="w"
)

course_entry = tk.Entry(form_frame, width=30)
course_entry.grid(row=2, column=1, padx=10, pady=10)


# Q.1 (i): Create buttons using grid()
button_frame = tk.Frame(root)
button_frame.pack(pady=15)

submit_button = tk.Button(
    button_frame,
    text="Submit",
    width=12,
    command=submit_form
)
submit_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(
    button_frame,
    text="Clear",
    width=12,
    command=clear_form
)
clear_button.grid(row=0, column=1, padx=10)


# Q.1 (j): Create text box and scrollbar
text_frame = tk.Frame(root)
text_frame.pack(pady=10)

scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text_box = tk.Text(
    text_frame,
    width=50,
    height=5,
    yscrollcommand=scrollbar.set
)
text_box.pack(side=tk.LEFT)

scrollbar.config(command=text_box.yview)


# Q.1 (k): Start the GUI application
root.mainloop()
