import tkinter as tk
import tkinter.messagebox
import sqlite3

# Initialize the main window
root = tk.Tk()
root.geometry('800x650')  # Set the window size
root.config(bg='#b6d7a8')  # Set the background color
root.title('PythonProject team -3')  # Set the window title
root.resizable(0, 0)  # Disable window resizing

# Create a connection to the SQLite database
conn = sqlite3.connect('contacts.db')  # Replace 'contacts.db' with your preferred database file name
cursor = conn.cursor()

# Create the contacts table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY,
        name TEXT,
        number TEXT,
        blood_group TEXT
    )
''')

# Define a list to store contact information
contactlist = []

# Create StringVar objects to store input field values
Name = tk.StringVar()
Number = tk.StringVar()
BloodGroup = tk.StringVar()

# Create a frame within the main window
frame = tk.Frame(root)
frame.pack(side=tk.RIGHT)

# Create a vertical scrollbar for the listbox
scroll = tk.Scrollbar(frame, orient=tk.VERTICAL)
# Create a Listbox widget with scrollbar, set font and appearance
select = tk.Listbox(frame, yscrollcommand=scroll.set, font=('Times new roman', 16), bg="#f0fffc", width=20, height=20,
                    borderwidth=3, relief="groove")
# Configure the scrollbar to scroll the Listbox
scroll.config(command=select.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
select.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# Function to get the index of the selected item in the Listbox
def Selected():
    if not select.curselection():
        tk.messagebox.showerror("Error", "Please Select the Name")
        return None
    return select.curselection()[0]

# Function to add a new contact to the database
def AddContact():
    if Name.get() and Number.get() and BloodGroup.get():
        cursor.execute("INSERT INTO contacts (name, number, blood_group) VALUES (?, ?, ?)",
                       (Name.get(), Number.get(), BloodGroup.get()))
        conn.commit()
        Select_set()
        EntryReset()
        tk.messagebox.showinfo("Confirmation", "Successfully Added New Contact")
    else:
        tk.messagebox.showerror("Error", "Please fill in the information")

# Function to edit an existing contact
def UpdateDetail():
    selected = Selected()
    if selected is not None:
        if Name.get() and Number.get() and BloodGroup.get():
            cursor.execute("UPDATE contacts SET name=?, number=?, blood_group=? WHERE id=?",
                           (Name.get(), Number.get(), BloodGroup.get(), contactlist[selected]))
            conn.commit()
            tk.messagebox.showinfo("Confirmation", "Successfully Updated Contact")
            EntryReset()
            Select_set()
        else:
            tk.messagebox.showerror("Error", "Please fill in the information")

# Function to reset input fields
def EntryReset():
    Name.set('')
    Number.set('')
    BloodGroup.set('')

# Function to delete the selected contact
def Delete_Entry():
    selected = Selected()
    if selected is not None:
        result = tk.messagebox.askyesno('Confirmation', 'You Want to Delete the Contact You Selected')
        if result:
            cursor.execute("DELETE FROM contacts WHERE id=?", (contactlist[selected],))
            conn.commit()
            Select_set()
    else:
        tk.messagebox.showerror("Error", 'Please select the Contact')

# Function to view contact details
def VIEW():
    selected = Selected()
    if selected is not None:
        cursor.execute("SELECT name, number, blood_group FROM contacts WHERE id=?", (contactlist[selected],))
        name, number, blood_group = cursor.fetchone()
        Name.set(name)
        Number.set(number)
        BloodGroup.set(blood_group)

# Function to exit the application and close the database connection
def EXIT():
    conn.close()
    root.destroy()

# Function to update the Listbox with current contact list from the database
def Select_set():
    cursor.execute("SELECT id, name FROM contacts")
    contactlist.clear()
    select.delete(0, tk.END)
    for row in cursor.fetchall():
        contactlist.append(row[0])
        select.insert(tk.END, row[1])

# Initial population of the Listbox
Select_set()

# Create labels, entry widgets, and buttons in the main window
tk.Label(root, text='Name', font=("Times new roman", 25, "bold"), bg='orange').place(x=30, y=20)
tk.Entry(root, textvariable=Name, width=30).place(x=200, y=30)
tk.Label(root, text='Contact No.', font=("Times new roman", 22, "bold"), bg='SlateGray3').place(x=30, y=70)
tk.Entry(root, textvariable=Number, width=30).place(x=200, y=80)
tk.Label(root, text='Blood Group', font=("Times new roman", 22, "bold"), bg='Red').place(x=30, y=120)
tk.Entry(root, textvariable=BloodGroup, width=30).place(x=200, y=130)
tk.Button(root, text=" ADD", font='Helvetica 18 bold', bg='#e8c1c7', command=AddContact, padx=20).place(x=50, y=190)
tk.Button(root, text="EDIT", font='Helvetica 18 bold', bg='#e8c1c7', command=UpdateDetail, padx=20).place(x=50, y=250)
tk.Button(root, text="DELETE", font='Helvetica 18 bold', bg='#e8c1c7', command=Delete_Entry, padx=20).place(x=50, y=310)
tk.Button(root, text="VIEW", font='Helvetica 18 bold', bg='#e8c1c7', command=VIEW).place(x=50, y=375)
tk.Button(root, text="RESET", font='Helvetica 18 bold', bg='#e8c1c7', command=EntryReset).place(x=50, y=440)
tk.Button(root, text="EXIT", font='Helvetica 24 bold', bg='tomato', command=EXIT).place(x=250, y=520)

# Start the Tkinter main loop
root.mainloop()
