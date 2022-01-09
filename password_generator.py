from tkinter import *
import string
import random
import pyperclip

password_chars = string.ascii_letters + string.digits + string.punctuation

def password_generator():
    password_field.delete(0, END)
    length = int(char_input.get())
    password = "".join([random.choice(password_chars) for _ in range(length)])
    password_field.insert(0, password)
    pyperclip.copy(password)

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50, bg="#383e56")

p1 = PhotoImage(file = 'key.png')

# Setting icon of master window
window.iconphoto(False, p1)

label_title = Label(text="Password Generator",
                    bg="#383e56",
                    fg="#c5d7bd",
                    font=("Fira Code", 35, "bold"))
label_title.grid(row=0, column=0, columnspan=3, pady=30)

char_input = Entry(bg="#fb743e")
char_input.insert(0, "16 ")
char_input.focus()

generate_password_button = Button(text="Generate Password & Copy to Clipboard",
                                  bg="#7289da",
                                  fg="#fff",
                                  height=4,
                                  width=55,
                                  command=password_generator, font=("Fira Code", 15, "bold"))
generate_password_button.grid(row=2, column=0, columnspan=3, padx=50, pady=50)

password_field = Entry(bg="#383e56",fg="#c5d7bd",
                       font=("Cascadia Code", 15, "bold"), width=40)
password_field.grid(row=3, column=0, columnspan=3)

window.mainloop()