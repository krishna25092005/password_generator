from tkinter import *
import string
import random
import pyperclip

def generator():
    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    all_chars = small_alphabets + capital_alphabets + numbers + special_characters
    password_length = int(length_Box.get())

    if choice.get() == 1:
        passwordField.delete(0, END)
        passwordField.insert(0, ''.join(random.sample(small_alphabets, password_length)))

    if choice.get() == 2:
        passwordField.delete(0, END)
        passwordField.insert(0, ''.join(random.sample(small_alphabets + capital_alphabets, password_length)))

    if choice.get() == 3:
        passwordField.delete(0, END)
        passwordField.insert(0, ''.join(random.sample(all_chars, password_length)))

def copy():
    random_password = passwordField.get()
    pyperclip.copy(random_password)

def toggle_password():
    if show_password.get():
        passwordField.config(show="")
    else:
        passwordField.config(show="*")

root = Tk()
root.config(bg='#263238') 
root.title('Random Password Generator')  # Set the title of the window

choice = IntVar()
show_password = BooleanVar()

Font = ('Hack', 13)  

passwordLabel = Label(root, text='Password Generator', font=('times new roman', 20, 'bold'), bg='#263238', fg='#00FF00') 
passwordLabel.grid(row=0, column=0, columnspan=3, pady=10)

weakradioButton = Radiobutton(root, text='Weak', value=1, variable=choice, font=Font, fg='#00FF00', bg='#263238', selectcolor='#37474F') 
weakradioButton.grid(row=1, column=0, pady=5)

mediumradioButton = Radiobutton(root, text='Medium', value=2, variable=choice, font=Font, fg='#00FF00', bg='#263238', selectcolor='#37474F')  
mediumradioButton.grid(row=1, column=1, pady=5)

strongradioButton = Radiobutton(root, text='Strong', value=3, variable=choice, font=Font, fg='#00FF00', bg='#263238', selectcolor='#37474F') 
strongradioButton.grid(row=1, column=2, pady=5)

lengthLabel = Label(root, text='Password Length', font=Font, bg='#263238', fg='#00FF00') 
lengthLabel.grid(row=2, column=0, pady=5)

length_Box = Spinbox(root, from_=5, to_=18, width=5, font=Font)
length_Box.grid(row=2, column=1, pady=5)

generateButton = Button(root, text='Generate', font=Font, command=generator, fg='#263238', bg='#00FF00') 
generateButton.grid(row=2, column=2, pady=5)

passwordField = Entry(root, width=25, bd=2, font=Font, show="*", fg='#00FF00', bg='#263238') 
passwordField.grid(row=3, column=0, columnspan=3, pady=5)

copyButton = Button(root, text='Copy', font=Font, command=copy, fg='#263238', bg='#00FF00') 
copyButton.grid(row=4, column=0, columnspan=2, pady=5)

toggleButton = Checkbutton(root, text='Show Password', variable=show_password, font=Font, fg='#00FF00', bg='#263238', selectcolor='#37474F', command=toggle_password) 
toggleButton.grid(row=4, column=2, pady=5)

root.mainloop()