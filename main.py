from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid()
canvas.grid_configure(row=0, column=1)

# Row 1
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.config(width=35)

# Row 2
email_username_label = Label(text="Email/Username:")
# email_username_label.config(width=30)
email_username_label.grid(column=0, row=2)

email_username_entry = Entry()
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.configure(width=35)

# Row 3
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry()
password_entry.grid(column=1, row=3)
password_entry.config(width=20)

password_button = Button(text="Generate password")
password_button.grid(column=2, row=3)
password_button



window.mainloop()
