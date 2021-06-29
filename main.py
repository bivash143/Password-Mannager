#! /usr/bin/python3
from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip


#generating random password

def pass_gen_button_fun():

    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '%', '&', '(', ')', '*', '+', '_', '-', '/']

    password_letters = [choice(letters) for x in range(randint(8, 10))]
    password_symbol = [choice(numbers) for x in range(randint(2, 4))]
    password_numbers = [choice(symbols) for x in range(randint(2, 4))]

    password_list = password_letters + password_symbol+ password_numbers

    shuffle(password_list)
    password = "".join(password_list)

    password_input.insert(0, string=password)


# adding data

def add_button_fun():
    website = website_input.get()
    email_username = email_username_input.get()
    password = password_input.get()

    is_ok_to_save = True
    if(len(website) == 0 or len(email_username) == 0 or len(password) == 0):
        messagebox.showerror(title="Oops...", message="Please Don't Leave Any Field Empty")
        is_ok_to_save = False

    if(is_ok_to_save):
        is_ok_to_save = messagebox.askyesno(title="Check the Details", message=f"Website: {website}\n Email/Username: {email_username}\n"
                                                                                f"Password: {password}\n Is It Ok To Save?")

    if(is_ok_to_save):
        pyperclip.copy(password)
        with open("./src/data.txt", "a") as file:
            file.write(f"\n{website}    |    {email_username}    |    {password}")

        website_input.delete(0, END)
        website_input.insert(END, string="www.")
        email_username_input.delete(0, END)
        password_input.delete(0, END)


#gui Design

window = Tk()
window.title("Password Mannager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="./src/password.png")
canvas.create_image(140, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ") 
website_label.grid(row=1, column=0)

website_input = Entry(width=43)
website_input.insert(END, string="www.")
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)

email_username_label = Label(text="Email/Username: ")
email_username_label.grid(row=2, column=0)

email_username_input = Entry(width=43)
email_username_input.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

password_input = Entry(width=24)
password_input.grid(row=3, column=1)

generate_pass_button = Button(text="Generate Password", command=pass_gen_button_fun)
generate_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=add_button_fun)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
