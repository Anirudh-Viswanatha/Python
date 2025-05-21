from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# -------------------------------- PASSWORD GENERATOR -----------------------------
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    for char in range(nr_letters):
      password_list.append(random.choice(letters))
      
    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    """
    # Option 2 using list comprehensions 
    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]   
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]   
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))] 


    # Option 3 list comprehensions + single range
    password_list = [random.choice(letters) + random.choice(symbols) + random.choice(numbers) for _ in range(5)]
    """

    random.shuffle(password_list)

    password = "".join(password_list) # help join contents in Lists, Tuples, Dictionaries
    password_input.insert(0,password)
    pyperclip.copy(password)




# -------------------------------- SAVE PASSWORD -----------------------------
def save_to_file():
      
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    
    if len(website) <=2 or len(password) <=4 or len(email) <= 4:
        messagebox.showinfo(title="Oops", message="Please enter valid inputs!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are details entered: \n \n Website:{website} \n Email:{email} \n Password: {password} \n \n  is it ok to save? ")
        if is_ok:    
            with open ("data.txt", "a") as datafile:
                datafile.write (f"{website} | {email} | {password} \n")
                website_input.delete(0,END)
                password_input.delete(0,END)
                email_input.delete(0,END)
                email_input.insert(0, "my_email@gmail.com")

# -------------------------------- UI SETUP -----------------------------
window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200,)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(140, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)

password_label = Label(text="Password")
password_label.grid(row=3, column=0)


# Inputs
website_input = Entry(width=36)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)

email_input = Entry(width=36)
email_input.insert(0, "my_email@gmail.com")
email_input.grid(row=2, column=1, columnspan=2)

password_input = Entry(width=19)
password_input.grid(row=3, column=1, columnspan=1)


# Buttons
Generate_password = Button(text="Generate Password", command=generate_password)
Generate_password.grid(row=3, column=2)

Add_button = Button(text="Add", width=36, command=save_to_file)
Add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
