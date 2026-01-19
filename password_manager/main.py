import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    from random import choice,randint,shuffle
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)    # <--- NEW WAY OF DOING

    # password = ""                  <---OLD WAYS OF DOING,
    # for char in password_list:
    #   password += char

    #print(f"Your password is: {password}")
    passw.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    if len(web.get())==0 or len(passw.get())==0 or len(mail.get())==0:
        messagebox.showinfo("Error", "All fields are mandatory, Do not leave any field blank")
    else:
        is_ok=messagebox.askokcancel(title=f'{web.get()}',
                                     message=f'The credentials entered are: '
                                     f'\nEmail: {mail.get()}\nPassword: {passw.get()}\n Are you sure you want'
                                     f' to add this?')
        if is_ok:
            with open('passwords.txt', 'a') as file:
                add_file=f'{web.get()} | {mail.get()} | {passw.get()}\n'
                file.write(add_file)
                web.delete(0, END)
                passw.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)
canvas=Canvas(height=200, width=200)
logo_png=PhotoImage(file="logo.png")
screen=canvas.create_image(100,100,image=logo_png)
canvas.grid(row=0,column=1)

website=Label(text="Website:")
website.grid(row=1,column=0)
web=Entry(width=45)
web.grid(row=1,column=1, columnspan=2)
web.focus()

email=Label(text="Email/Username:")
email.grid(row=2,column=0)
mail=Entry(width=45)
mail.grid(row=2,column=1, columnspan=2)
mail.insert(0,"pavanreddy694829@gmail.com")

password_label=Label(text="Password:       ")
password_label.grid(row=3,column=0)
passw=Entry(width=27)
passw.grid(row=3,column=1)

generate=Button(text="Generate Password",command=generate_password)
generate.grid(row=3,column=2)

add=Button(width=36,text="Add",command=save)
add.grid(row=4,column=1,columnspan=2)
canvas.itemconfig(screen)





















window.mainloop()