from tkinter import *
from tkinter import messagebox
import random
import pyperclip  # To copy password to clipboard

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'
    
    password_list = (
        [random.choice(letters) for _ in range(8)] +
        [random.choice(symbols) for _ in range(2)] +
        [random.choice(numbers) for _ in range(2)]
    )
    random.shuffle(password_list)
    password = ''.join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)  # Copies the password to the clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure no field is empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Details entered:\nEmail: {email}\nPassword: {password}\nSave?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0, padx=5, pady=5)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0, padx=5, pady=5)
password_label = Label(text="Password")
password_label.grid(row=3, column=0, padx=5, pady=5)

# Entries
website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)
website_entry.focus()
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=5)
email_entry.insert(0, "abhijeetpanigrahi912@gmail.com")
password_entry = Entry(width=34)
password_entry.grid(row=3, column=1, padx=5, pady=5)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
