import json
from tkinter import Button, Label, Entry
from canvas import tk
from helpers import clean_screen
from products import render_products


def render_main_enter_screen():
    Button(tk, text="Login", font=('Arial', 12), width=10,
           bg="blue", fg="white", command=render_login).grid(row=0, column=0)
    Button(tk, text="Register", font=('Arial', 12), width=10,
           bg="red", fg="white", command=render_register).grid(row=0, column=1)


def render_login(errors=False):
    clean_screen()
    Label(tk, text="Username", font=('Arial', 12), width=10, bg="white", fg="blue").grid(row=0, column=0)
    username = Entry(tk)
    username.grid(row=0, column=1)
    Label(tk, text="Password", font=('Arial', 12), width=10, bg="white", fg="blue").grid(row=1, column=0)
    password = Entry(tk, show="*")
    password.grid(row=1, column=1)
    Button(tk, text="Enter", font=('Arial', 12), width=10, bg="blue", fg="white",
           command=lambda: login(username.get(), password.get())).grid(row=2, column=1)
    if errors:
        Label(tk, text="Invalid username or password!", font=('Arial', 12),
              bg="black", fg="blue").grid(row=3, column=2)


def render_register():
    clean_screen()
    Label(tk, text="Username", font=('Arial', 12), width=10, bg="white", fg="red").grid(row=0, column=0)
    username = Entry(tk)
    username.grid(row=0, column=1)
    Label(tk, text="Password", font=('Arial', 12), width=10, bg="white", fg="red").grid(row=1, column=0)
    password = Entry(tk, show="*")
    password.grid(row=1, column=1)
    Label(tk, text="First name", font=('Arial', 12), width=10, bg="white", fg="red").grid(row=2, column=0)
    first_name = Entry(tk)
    first_name.grid(row=2, column=1)
    Label(tk, text="Last name", font=('Arial', 12), width=10, bg="white", fg="red").grid(row=3, column=0)
    last_name = Entry(tk)
    last_name.grid(row=3, column=1)
    Button(tk, text="Enter", font=('Arial', 12), width=10, bg="red", fg="white",
           command=lambda: register(username=username.get(),
                                    password=password.get(),
                                    first_name=first_name.get(),
                                    last_name=last_name.get())).grid(row=4, column=1)


def login(username, password):
    with open("db/user_credentials_db.txt", "r") as file:
        for line in file.readlines():
            name, pswd = line[:-1].split(", ")
            if name == username and pswd == password:
                with open("db/curr_user.txt", "w") as curr_user_file:
                    curr_user_file.write(username)
                render_products()
                return
    render_login(errors=True)


def register(**user):
    user.update({"products": []})
    with open("db/users.txt", "a") as file:
        file.write(json.dumps(user))
        file.write("\n")
    with open("db/user_credentials_db.txt", "a") as file:
        file.write(f"{user['username']}, {user['password']}")
        file.write("\n")
    render_login()

