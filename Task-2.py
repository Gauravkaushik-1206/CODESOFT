from tkinter import *

root = Tk()
root.geometry("350x350")
root.maxsize(350, 350)
root.title("Calculator")

value = StringVar()
value.set("")

screen = Entry(root, textvar=value, font="lucida 30 bold")
screen.pack(fill=X, ipadx=8, padx=10, pady=10)

# create buuton frame
button_frame = Frame(root)
button_frame.pack()


# Functions
def click(event):
    global value
    text = event.widget.cget("text")
    if text == "=":
        if value.get().isdigit():
            answer = int(value.get())
        else:
            try:
                answer = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"

        value.set(answer)
        screen.update()

    elif text == "C":
        value.set("")
        screen.update()

    else:
        value.set(value.get() + text)
        screen.update()


# create buuton in the frame
b_C = Button(button_frame, width=3, text="C", font="lucida 25 bold")
b_C.grid(row=0, column=0)
b_C.bind("<Button-1>", click)

b_equal = Button(button_frame, width=3, text="=", font="lucida 25 bold")
b_equal.grid(row=0, column=1)
b_equal.bind("<Button-1>", click)

b_0 = Button(button_frame, width=3, text="0", font="lucida 25 bold")
b_0.grid(row=0, column=2)
b_0.bind("<Button-1>", click)

b_div = Button(button_frame, width=3, text="/", font="lucida 25 bold")
b_div.grid(row=0, column=3)
b_div.bind("<Button-1>", click)

b_7 = Button(button_frame, width=3, text="7", font="lucida 25 bold")
b_7.grid(row=1, column=0)
b_7.bind("<Button-1>", click)

b_8 = Button(button_frame, width=3, text="8", font="lucida 25 bold")
b_8.grid(row=1, column=1)
b_8.bind("<Button-1>", click)

b_9 = Button(button_frame, width=3, text="9", font="lucida 25 bold")
b_9.grid(row=1, column=2)
b_9.bind("<Button-1>", click)

b_sub = Button(button_frame, width=3, text="-", font="lucida 25 bold")
b_sub.grid(row=1, column=3)
b_sub.bind("<Button-1>", click)

b_4 = Button(button_frame, width=3, text="4", font="lucida 25 bold")
b_4.grid(row=2, column=0)
b_4.bind("<Button-1>", click)

b_5 = Button(button_frame, width=3, text="5", font="lucida 25 bold")
b_5.grid(row=2, column=1)
b_5.bind("<Button-1>", click)

b_6 = Button(button_frame, width=3, text="6", font="lucida 25 bold")
b_6.grid(row=2, column=2)
b_6.bind("<Button-1>", click)

b_add = Button(button_frame, width=3, text="+", font="lucida 25 bold")
b_add.grid(row=2, column=3)
b_add.bind("<Button-1>", click)

b_1 = Button(button_frame, width=3, text="1", font="lucida 25 bold")
b_1.grid(row=3, column=0)
b_1.bind("<Button-1>", click)

b_2 = Button(button_frame, width=3, text="2", font="lucida 25 bold")
b_2.grid(row=3, column=1)
b_2.bind("<Button-1>", click)

b_3 = Button(button_frame, width=3, text="3", font="lucida 25 bold")
b_3.grid(row=3, column=2)
b_3.bind("<Button-1>", click)

b_multi = Button(button_frame, width=3, text="*", font="lucida 25 bold")
b_multi.grid(row=3, column=3)
b_multi.bind("<Button-1>", click)

root.mainloop()
