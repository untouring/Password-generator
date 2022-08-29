from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_function():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_letters = [choice(letters) for i in range(randint(1, 52))]
    password_numbers = [choice(numbers) for k in range(randint(1, 9))]
    password_symbols = [choice(symbols) for l in range(randint(1, 8))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password_d = "".join(password_list)

    password_entry.insert(0, password_d)

    pyperclip.copy(password_d)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_function():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops... error", message="The fields are empty!")
    else:

        is_saved = messagebox.askokcancel(title="Is it right?", message=f"These are the details entered: \n Website: {website},\n Email: {email},\n Password: {password}. \nShould it be saved?")

        if is_saved:
            with open("passwords.txt", "a") as passwords_file:
                passwords_file.write(f'{website} | {email} | {password}\n')
                website_entry.delete(0, END)
                password_entry.delete(0, END)
        elif is_saved == False:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="password_logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)

password_label = Label(text="Password")
password_label.grid(column=0, row=3)

add_button = Button(text="Add", width=36, command=add_function)
add_button.grid(column=1, row=4, columnspan=2)

generate_password = Button(text="Generate Password", command=generate_function)
generate_password.grid(column=2, row=3)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, columnspan=1)

email_entry = Entry(width=35)
email_entry.insert(0, "architect.best@yandex.ru")
email_entry.grid(column=1, row=2, columnspan=2)



window.mainloop()
