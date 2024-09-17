from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  password_letters = [choice(letters) for _ in range(randint(0,10))]
  password_symbols = [choice(letters) for _ in range(randint(2, 4))]
  password_numbers = [choice(letters) for _ in range(randint(2, 4))]

  password = password_letters + password_symbols + password_numbers
  shuffle(password)

  new_password ="".join(password)
  password_entry.insert(0,new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_passwords():
  website = website_entry.get()
  password = password_entry.get()
  email = email_entry.get()
  new_data = {
    website: {
      "email": email,
      "password":password,
    }
  }


  if len(website) == 0 or len(password)  == 0:
    messagebox.showinfo(title="Oops",message="Please dont leave any fields empty")

  else:
    try:
      with open("data.json","r") as data_file:
        data =json.load(data_file)

    except FileNotFoundError:
      with open("data.json","w") as data_file:
        json.dump(new_data,data_file,indent=4)

    else:
      data.update(new_data)
      with open("data.json","w") as data_file:
          json.dump(data,data_file,indent=4)

    finally:
        website_entry.delete(0,END)
        password_entry.delete(0,END)
        email_entry.delete(0,END)

def find_password():
  website = website_entry.get()
  try:
    with open("data.json") as data_file:
      data = json.load(data_file)
  except FileNotFoundError:
     messagebox.showinfo(title="Error",message="No password found")
  else:
    if website in data:
      email = data[website]["email"]
      password =data[website]["password"]
      messagebox.showinfo(title="Password",message=f"Email: {email}\nPassword:{password}")
    else:
      messagebox.showinfo(title="Error",message=f"no details for {website} exists")

  website_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)


Canvas = Canvas(width=200,height=200)
logo_img = PhotoImage(file="logo.png")
Canvas.create_image(100,100,image=logo_img)
Canvas.grid(column=1,row=0)

# website label
website_label = Label(text="Website:")
website_label.grid(column=0,row=1)

# website entry
website_entry = Entry(width=21)
website_entry.grid(column=1,row=1)
website_entry.focus()


# Email/username label
email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)


# Email/username entry
email_entry = Entry(width=45)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.focus()
email_entry.insert(0,"ragha@gmail.com")

# Password label
password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

# password entry
password_entry = Entry(width=21)
password_entry.grid(column=1,row=3)
password_entry.focus()


# generate button
Generate_button = Button(text="Generate Password",command=generate_password,width=20)
Generate_button.grid(column=2,row=3)

# add button
Add_button = Button(text="Add",width=45,command=save_passwords)
Add_button.grid(column=1,row=4,columnspan=2)

# search button
search_button = Button(text="search",width=20,command=find_password)
search_button.grid(column=2,row=1)






window.mainloop()
