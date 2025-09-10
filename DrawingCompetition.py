# import modules
from tkinter import *
from tkinter import messagebox
from datetime import datetime
import os
import csv
import subprocess

# define functions
def mouse_drawing(event):
    # Get position of cursor
    x_pos = event.x
    y_pos = event.y

    # Sets coordinates of the circle to be placed
    x1 = x_pos - 2
    x2 = x_pos + 2
    y1 = y_pos - 2
    y2 = y_pos + 2

    # Create a small circle
    canvas.create_oval(x1, y1, x2, y2, fill="black")

def submit_drawing():
    # Bring global values into the function
    global permission
    global gender
    global occupation

    # Check for permission and non-null values in the data entry section
    if permission.get() == 0:
        messagebox.showinfo("Permission Not Given", "Please give permission for data to be taken.")
    elif gender == "N" or occupation == "N" or fn_entry.get() == "" or ln_entry.get() == "":
        messagebox.showinfo("Missing Data", "Please fill out all parts of the data entry")
    else:
        messagebox.showinfo("Submitted", "Drawing and data submitted, thank you for playing!")

        # Creates the file name of the drawing from submitted data and the current date and time
        date_time = datetime.now()
        artist = fn_entry.get() + ln_entry.get()

        year = date_time.year
        month = date_time.month
        day = date_time.day
        hour = date_time.hour
        minute = date_time.minute

        file_name = f"{artist}:{year}-{month:02d}-{day:02d}_{hour:02d}:{minute:02d}"

        # Runs functions to export drawing and data
        export_drawing(file_name)
        export_details(file_name)

def export_drawing(file_name):
        # Creates file names for .ps and .png drawings
        file_name_ps = file_name + ".ps"
        file_name_png = file_name + ".png"

        # Save drawing (has to save in .ps format)
        canvas.postscript(file=file_name_ps, colormode='color')

        # Convert to jpg
        subprocess.run([
            "/opt/homebrew/bin/gs",  # path to ghostscript
            "-dSAFER",
            "-dBATCH",
            "-dNOPAUSE",
            "-sDEVICE=png16m",
            "-r300",  # resolution (DPI)
            "-sOutputFile="+file_name_png,
            file_name_ps
        ])

        # Deletes .ps file after png has been created
        if os.path.isfile(file_name_ps):
            os.remove(file_name_ps)

def export_details(file_name):
    # Checks if csv file exists
    file_exists = os.path.isfile("Submissions.csv")

    # Prepare data for entry to file
    dob = f"{birth_day_spinbox.get()}-{birth_month_spinbox.get()}-{birth_year_spinbox.get()}"
    data_row = [fn_entry.get(),ln_entry.get(),gender.get(),occupation.get(),dob,file_name]

    # Makes new file and includes header if no file exists, if file does exists it simply adds data on to the end
    if file_exists:
        with open("Submissions.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(data_row)
    else:
        with open("Submissions.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["First Name", "Last Name", "Gender", "Occupation", "Date of Birth", "Submission Name"])
            writer.writerow(data_row)

def clear_canvas():
    # Check if user really wants to clear drawing
    clear = messagebox.askyesno("Warning", "Are you sure you want to clear your drawing?")

    # If they do then clear the drawing
    if clear:
        canvas.delete("all")


# create window
window = Tk()
window.title("Art Competition - Python GUI")
# window.geometry("750x250")

# create a frame to place objects in and keep everything central
content = Frame(window)
content.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

# define all global tkinter variables
gender = StringVar()
gender.set("N")
occupation = StringVar()
occupation.set("N")
permission = IntVar()
permission.set(0)

# create and layout radio button widgets for gender
male_label = Label(content, text="Male")
male_radiobutton = Radiobutton(content, variable = gender, value= "Male")
female_label = Label(content, text="Female")
female_radiobutton = Radiobutton(content, variable= gender, value= "Female")
unspec_label = Label(content, text="Unspecified")
unspec_radiobutton = Radiobutton(content, variable = gender, value = "Unspecified")

# create and layout radio button widgets for occupation
student_label = Label(content, text="Student")
student_radiobutton = Radiobutton(content, variable = occupation, value= "Student")
wb_label = Label(content, text="Worker Bee")
wb_radiobutton = Radiobutton(content, variable= occupation, value= "Worker Bee")
inf_label = Label(content, text="Influencer")
inf_radiobutton = Radiobutton(content, variable = occupation, value = "Influencer")

# create and layout radio button widgets for permission
permission_label = Label(content, text="Permission to collect data?")
permission_radiobutton = Checkbutton(content, variable = permission, onvalue= 1)


# create canvas widget
canvas = Canvas(content, bg="lightblue")

# create name, birthday, clear and confirm widgets
fn_label = Label(content, text="First Name:")
fn_entry = Entry(content)
ln_label = Label(content, text="Last Name:")
ln_entry = Entry(content)

bd_label = Label(content, text="Date of Birth:")

clear_button = Button(content, text="Clear", command=clear_canvas)

submit_button = Button(content, text='Submit?', command=submit_drawing)

# create a frame widget to hold the birth_date spinboxes
birth_date_frame = Frame(content)
birth_day_spinbox = Spinbox(birth_date_frame, from_=1, to=31, width=2)
birth_month_spinbox = Spinbox(birth_date_frame, from_=1, to=12, width=2)
birth_year_spinbox = Spinbox(birth_date_frame, from_=1900, to=2010, width=4)

birth_day_spinbox.pack(side=LEFT)
birth_month_spinbox.pack(side=LEFT)
birth_year_spinbox.pack(side=LEFT)


# place widgets into window container using the grid layout
fn_label.grid(row=0,column=0)
fn_entry.grid(row=0,column=1)
ln_label.grid(row=1,column=0)
ln_entry.grid(row=1,column=1)

bd_label.grid(row=2, column=0)
birth_date_frame.grid(row=2,column=1)

male_label.grid(row=3,column=0)
male_radiobutton.grid(row=4,column=0)
female_label.grid(row=3,column=1)
female_radiobutton.grid(row=4,column=1)
unspec_label.grid(row=3,column=2)
unspec_radiobutton.grid(row=4,column=2)

student_label.grid(row=5,column=0)
student_radiobutton.grid(row=6,column=0)
wb_label.grid(row=5,column=1)
wb_radiobutton.grid(row=6,column=1)
inf_label.grid(row=5,column=2)
inf_radiobutton.grid(row=6,column=2)

permission_label.grid(row=8,column=0)
permission_radiobutton.grid(row=8,column=1)

clear_button.grid(row=9,column=7)

submit_button.grid(row=9,column=1,padx=30)

canvas.grid(row=0,column=3,rowspan=9,columnspan=9)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# bind widget events to functions
canvas.bind("<B1-Motion>", mouse_drawing)

# open window
window.mainloop()
