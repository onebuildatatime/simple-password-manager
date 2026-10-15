from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for item in range(randint(8, 10))]
    password_symbols = [choice(symbols) for item in range(randint(2, 4))]
    password_numbers = [choice(numbers) for item in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    print(f"Your password is: {password}")
    pyperclip.copy(password)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(window, width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)
pass_label = Label(text="Password:")
pass_label.grid(row=3,column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1,column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    if not website or not email or not password:
        messagebox.showwarning(
            title="Missing Information",
            message="Please fill in all fields before saving.",
        )
        return

    is_ok = messagebox.askokcancel(
        title=website,
        message=(
            f"Website: {website}\n"
            f"Email/Username: {email}\n"
            f"Password: {password}\n\n"
            "Save these details?"
        ),
    )

    if is_ok:
        with open("password.txt", "a") as file:
            file.write(f"{website} | {email} | {password}\n")

        messagebox.showinfo(
            title="Success",
            message=f"Password for {website} was saved.",
        )

        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()

#Buttons
generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=3,column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4,column=1)






window.mainloop()
