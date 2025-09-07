from tkinter import *
from tkinter import messagebox
from random import randint , choice , shuffle
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    password_letters = [ choice(letters) for _ in range(randint(8 , 10))]
    password_numbers = [ choice(numbers) for _ in range(randint(2 , 4))]
    password_symbols = [ choice(symbols) for _ in range(randint(2 , 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    new_password = "".join(password_list)
    password_text.delete(0 , END)
    password_text.insert(0 , new_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_website = website_text.get()
    new_email = email_text.get()
    new_pass = password_text.get()
    if len(new_website) == 0 or len(new_pass) == 0 :
        messagebox.showinfo(title="Oops" ,  message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=new_website, message=f"These are the details entered: \nEmail: {new_email} "
                                        f"\nPassword: {new_pass} \nIs it ok to save?")    
        if is_ok:
            with open("Day_29\data.txt" , "a") as data_file:
                data_file.write(f"{new_website} | {new_email} | {new_pass}\n")
                website_text.delete(0, END)
                password_text.delete(0, END)
                
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config( pady=20 , padx = 20)

canvas =Canvas(width=200 , height=200 )
new_image = PhotoImage(file="C:/Users/Ahmed/100_Days/Day_29/logo.png")
canvas.create_image(100 , 100 , image=new_image )
canvas.grid(column=1 , row=0 )

website_text = Entry(width=35)
website_text.grid(column=1 , row=1 , columnspan=2 , sticky="ew", pady=5)
website_text.focus()
website = Label(text="Website :")
website.grid(column=0 , row=1 )

email_text = Entry(width=35)
email_text.grid(column=1 , row=2 , columnspan=2, sticky="ew", pady=5)
email_text.insert(0 , "ahmedabdelkadersolia@gmail.com")
email = Label(text="Email/Username :")
email.grid(column=0 , row=2 )

password_text = Entry(width=31)
password_text.grid(column=1 , row=3, sticky="w" , pady=5)
password = Label(text="Password :")
password.grid(column=0 , row=3 )

Generate = Button(text="Generate Password" , command=generate_password)
Generate.grid(column=2 , row=3 , pady=5)

add = Button(text="ADD" ,width=36 , command= save )
add.grid(column=1 , row=4 , columnspan=2, sticky="ew" , pady=5)

window.mainloop()