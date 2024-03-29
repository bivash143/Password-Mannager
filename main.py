#! /usr/bin/python3
from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json


#search password

def search_pass():

    searing_item = website_input.get()

    try:
        
        with open("./src/data.json", "r") as file:
            data = json.load(file)

            if searing_item not in data:
                raise ValueError

    except ValueError:
        messagebox.showinfo(title="Something Went Wrong", message="No Data Present, Please Insert Data")

    except FileNotFoundError:
        messagebox.showinfo(title="Something Went Wrong", message="No Data Present, Please Insert Data")

    else:

        if searing_item in data:
            website = data[searing_item]
            email = website["email"]
            password = website["password"]

            messagebox.showinfo(title=searing_item, message=f"Email: {email}\nPassword: {password}")


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

    if(len(website) == 0 or len(email_username) == 0 or len(password) == 0):
        messagebox.showerror(title="Oops...", message="Please Don't Leave Any Field Empty")

    else:
        is_ok_to_save = messagebox.askyesno(title="Check the Details", message=f"Website: {website} \nEmail/Username: {email_username}\n"
                                                                                f"Password: {password}\n\n Is It Ok To Save?") 
        new_data = {
                        website:{
                            "email": email_username,
                            "password" : password,
                        }
        }

        if(is_ok_to_save):
            pyperclip.copy(password)

            try:
                
                with open("./src/data.json", "r") as file:
                    data = json.load(file)

            except:
                with open("./src/data.json", "w") as file:
                    json.dump(new_data, file, indent=4)

            else:
                data.update(new_data)
                with open("./src/data.json", "w") as file:
                    json.dump(data, file, indent=4)

            finally:
                website_input.delete(0, END)
                website_input.insert(END, string="www.")
                email_username_input.delete(0, END)
                password_input.delete(0, END)


#gui Design

window = Tk()
window.title("Password Mannager")
window.config(padx=50, pady=50, bg="#364547")

canvas = Canvas(width=205, height=200, bg="#364547", highlightthickness=0)
logo = PhotoImage(file="./src/password.png")
canvas.create_image(140, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ", bg="#364547", fg="white") 
website_label.grid(row=1, column=0, pady=5, padx=5)

website_input = Entry(width=24)
website_input.insert(END, string="www.")
website_input.focus()
website_input.grid(row=1, column=1, pady=5, padx=5)

password_search = Button(text="Search", width=16, command=search_pass, bg="#444444", fg="white")
password_search.grid(row=1, column=2, pady=5, padx=5)

email_username_label = Label(text="Email/Username: ", bg="#364547", fg="white")
email_username_label.grid(row=2, column=0, pady=5, padx=5)

email_username_input = Entry(width=44)
email_username_input.grid(row=2, column=1, columnspan=2, pady=5, padx=5)

password_label = Label(text="Password: ", bg="#364547", fg="white")
password_label.grid(row=3, column=0, pady=5, padx=5)

password_input = Entry(width=24)
password_input.grid(row=3, column=1, pady=5, padx=5)

generate_pass_button = Button(text="Generate Password", command=pass_gen_button_fun, bg="#444444", fg="white")
generate_pass_button.grid(row=3, column=2, pady=5, padx=5)

add_button = Button(text="Add", width=36, command=add_button_fun, bg="#444444", fg="white")
add_button.grid(row=4, column=1, columnspan=2, pady=5, padx=5)

window.mainloop()
