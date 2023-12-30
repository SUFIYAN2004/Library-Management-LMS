from tkinter import *


def next():
    import gi
    window.destroy()


window = Tk()
window.title("page_in")
window.geometry("1275x640+0+0")
window.config(bg="black")
window.resizable(0, 0)
logo = PhotoImage(file='cahc2.png')

Label(window, image=logo).place(x=600, y=50)

Label(window, text="C.Abdul Hakeem College", font=("Times new roman", 20, "italic"),
      fg="white", bg="black").place(x=530,  y=220)
Label(window, text="Dept. of Computer Science &", font=("Times new roman", 20, "italic"),
      fg="white", bg="black").place(x=480, y=280)
Label(window, text="Application Library", font=("Times new roman", 20, "italic"),
      fg="white", bg="black").place(x=660, y=330)
"""Label(window, text="Mr. K. Abdul Ahed", font=("Times new roman", 15, "italic"),
      fg="white", bg="black").place(x=100,  y=320)"""
button = Button(window, text="Get Started!", font=("Times new roman", 15, "italic"),
                width=27, command=next).place(x=520, y=400)
Label(window, text="Developed by:Sufiyan", font=("Times new roman", 15, "italic"),
      fg="white", bg="black").place(x=1000, y=500)

window.mainloop()