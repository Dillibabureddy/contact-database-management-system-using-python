Contact Management System

This is a simple Contact Management System built using Python and Tkinter with SQLite as the database.

Features

Add new contacts with Name, Contact Number, and Blood Group.

Edit existing contact details.

Delete contacts from the database.

View contact details.

Reset input fields.

Exit the application safely.

Prerequisites

Ensure you have Python installed on your system. You can download it from python.org.

Installation

Clone this repository:

git clone https://github.com/yourusername/contact-management-system.git

Navigate to the project directory:

cd contact-management-system

Install required dependencies (if needed):

pip install tk

Usage

Run the script using the following command:

python contact_manager.py

Project Structure

contact-management-system/
│-- contact_manager.py  # Main Python file with Tkinter UI
│-- contacts.db         # SQLite database file (created after running the script)
│-- README.md           # Project documentation

Database

This project uses an SQLite database (contacts.db) to store contact details. The database is automatically created if it doesn't exist.

Contributing

Feel free to contribute by submitting issues or pull requests.
