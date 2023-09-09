from tkinter import *
import string
import random


def generate_password():
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    password.set("".join(s[0:len.get()]))


root = Tk()
root.title("Password Generator")
root.geometry("350x350")
root.maxsize(350, 350)

l1 = Label(root, text="Enter the length of the password", font="comicsansms 15 bold", bg="blue", borderwidth=5, relief=SUNKEN)
l1.pack(pady=10)

len = IntVar()

len_screen = Entry(root, textvariable=len, font="comicsansms 20 bold")
len_screen.pack(pady=20)

password = StringVar()
l2 = Label(root, text="Generated Password", font="comicsansms 15 bold", bg= "red", borderwidth=5, relief=SUNKEN)
l2.pack(pady=10)

pass_screen = Entry(root, textvariable=password, font="comicsansms 20 bold")
pass_screen.pack(pady=20)

b1 = Button(root, text="Generate password", command=generate_password, bg="green", font="comicsansms 10 bold")
b1.pack(pady=10)
root.mainloop()
