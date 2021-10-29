import json
import os
from tkinter import Button, Label
from canvas import tk
from helpers import clean_screen
from PIL import Image, ImageTk


def buy_product(button):
    _, product_id = button.cget("text").split()
    product_id = int(product_id)
    with open("db/curr_user.txt", "r") as file:
        logged_user = file.read()
    with open("db/users.txt", "r+") as file:
        users = file.readlines()
        file.seek(0)
        for user in users:
            curr_user = json.loads(user)
            if curr_user.get('username') == logged_user:
                curr_user['products'].append(product_id)
            file.write(json.dumps(curr_user))
            file.write("\n")
    with open("db/products.txt", "r+") as file:
        products = file.readlines()
        file.seek(0)
        for product in products:
            curr_product = json.loads(product)
            if curr_product.get("id") == product_id:
                curr_product["count"] -= 1
            file.write(json.dumps(curr_product))
            file.write("\n")

    render_products()


def render_products():
    clean_screen()
    with open("db/products.txt", "r") as file:
        row_counter = 0
        column_counter = 0
        products = file.readlines()
        for product in products:
            curr_product = json.loads(product)
            Label(tk, text=curr_product.get("name"), font=('Arial', 12), width=10,
                  bg="white", fg="orange").grid(row=row_counter + 0, column=column_counter)
            image = Image.open(os.path.join(os.path.join(os.path.dirname(__file__), "images"),
                                            curr_product.get("image_path")))
            image = image.resize((100, 100))
            photo = ImageTk.PhotoImage(image)
            image_label = Label(image=photo)
            image_label.image = photo
            image_label.grid(row=row_counter + 1, column=column_counter)
            Label(tk, text=curr_product.get('count'), font=('Arial', 12), width=10,
                  bg="white", fg="orange").grid(row=row_counter + 2, column=column_counter)
            button = Button(tk, text=f"Buy {curr_product.get('id')}",
                            font=('Arial', 12), width=10, bg="orange", fg="white")
            button.configure(command=lambda b=button: buy_product(b))
            button.grid(row=row_counter + 3, column=column_counter)
            column_counter += 1
            if column_counter == 2:
                column_counter = 0
                row_counter += 4
