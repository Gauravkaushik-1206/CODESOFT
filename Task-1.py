from tkinter import *
from tkinter.font import Font

root = Tk()
root.title('To do List')
root.geometry("500x500")
root.maxsize(500, 450)

# Define font
my_font = Font(family="Brush Script MT", size=30, weight="bold")

# create frame
frame1 = Frame(root, width=50, bg="black", height=5, borderwidth=9, relief=SUNKEN)
frame1.pack()

label1 = Label(frame1, text="Tasks", bg="#00FFFF", fg="white", font="comicsansms 20 bold", borderwidth=9, relief=SUNKEN)
label1.pack()

# create listbox for tasks
lbx = Listbox(frame1,
              width=24,
              borderwidth=5,
              height=3,
              relief=SUNKEN,
              font=my_font,
              highlightthickness=0,
              selectbackground="blue",
              activestyle="none")
lbx.pack(side=LEFT, fill=BOTH)

# create scrollbar
scroll_bar = Scrollbar(frame1)
scroll_bar.pack(side=RIGHT, fill=BOTH)

# Add scrollbar
lbx.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=lbx.yview)

label1 = Label(root, text="Enter the Task", bg="#FF8000", fg="white", font="comicsansms 15 bold", borderwidth=5,
               relief=SUNKEN)
label1.pack(pady=5)


def add_item():
    lbx.insert(END, task.get());
    task.set("")


# create a enty box to add items
task = StringVar()
task.set("")

entry_frame = Frame(root)
entry_frame.pack(pady=10)

entry_box = Entry(entry_frame, textvar=task, borderwidth=5, font="comicsansms 20 bold")
entry_box.pack(pady=10, side=LEFT)
add_button = Button(entry_frame, text="ADD", command=add_item)
add_button.pack(side=LEFT)
# create a button frame
button_frame = Frame(root)
button_frame.pack(pady=10)


# Functions
def submit_item():
    lbx.insert(ACTIVE, task.get())
    task.set("")


def delete_item():
    lbx.delete(ANCHOR)


def edit_item():
    task.set(lbx.get(ANCHOR))
    lbx.delete(ANCHOR)


# Add buttons

submit_button = Button(button_frame, text="SUBMIT", command=submit_item, bg="green", font="comicsansms 10 bold")
delete_button = Button(button_frame, text="DELETE", command=delete_item, bg="red", font="comicsansms 10 bold")
edit_button = Button(button_frame, text="EDIT", command=edit_item, bg="blue", font="comicsansms 10 bold")

submit_button.grid(row=0, column=0)
delete_button.grid(row=0, column=1, padx=20)
edit_button.grid(row=0, column=2)

root.mainloop()
