import pyperclip,json
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
#----------------------------- FIND PASSWORD --------------------------------#
def find_password():
    website_data = web.get()
    try:
        with open('data.json') as json_file:
            saved=json.load(json_file)
    except FileNotFoundError:
        messagebox.showerror("Error", "No Data File Found.")
    else:
        if website_data in saved:
            messagebox.showinfo("Credentials", f"Email: {saved[website_data]["Email"]}\nPassword: {saved[website_data]["Password"]}")
        else:
            messagebox.showerror(title="Error", message="No credentials found for this website")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website_data=web.get()
    email_data=mail.get()
    password_data=passw.get()
    new_data={
        website_data:{
            'Email':email_data,
            'Password':password_data
        }
    }
    if len(web.get())==0 or len(passw.get())==0 or len(mail.get())==0:
        messagebox.showinfo("Error", "All fields are mandatory, Do not leave any field blank")
    else:
        try:
            with open("data. json", "r") as json_file:
                #Reading old data
                data = json.load(json_file)
        except FileNotFoundError:
            with open("data. json", "w") as json_file:
                json.dump(new_data, json_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as json_file:
                #Saving updated data
                json.dump(data, json_file, indent=4)
        finally:
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
web=Entry(width=30)
web.grid(row=1,column=1, columnspan=1)
web.focus()

email=Label(text="Email/Username:")
email.grid(row=2,column=0)
mail=Entry(width=48)
mail.grid(row=2,column=1, columnspan=2)
mail.insert(0,"pavanreddy694829@gmail.com")

password_label=Label(text="Password:       ")
password_label.grid(row=3,column=0)
passw=Entry(width=30)
passw.grid(row=3,column=1)

search=Button(text="Search",width=14,command=find_password)
search.grid(row=1,column=2)

generate=Button(text="Generate Password",command=generate_password)
generate.grid(row=3,column=2)

add=Button(width=36,text="Add",command=save)
add.grid(row=4,column=1,columnspan=2)
canvas.itemconfig(screen)























window.mainloop()