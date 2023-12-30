from tkinter import *
from tkinter import ttk, Tk
from tkinter import Frame, Listbox, Scrollbar
import mysql.connector
from tkinter import messagebox


class LibraryManagementSystem:
    def __init__(self, window):
        self.window = window
        self.window.title("Library Management System")
        self.window.geometry("1275x640+0+0")




# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Variable>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        self.member_var = StringVar()
        self.Prn_var = StringVar()
        self.ID_var = StringVar()
        self.First_var = StringVar()
        self.Last_var = StringVar()
        self.address_var = StringVar()
        self.pin_var = StringVar()
        self.mobile_var = StringVar()
        self.BookID_var = StringVar()
        self.BookTitle_var = StringVar()
        self.Author_var = StringVar()
        self.Date_Borrow_var = StringVar()
        self.DateDue_var = StringVar()
        self.DaysBook_var = StringVar()
        self.LastReturnFine_var = StringVar()
        self.DateOver_var = StringVar()

        def showdata(self):
            self.textbox.insert(END, "MemberType\t\t" + self.member_var.get() + "\n")
            self.textbox.insert(END, "PrnNo\t\t" + self.Prn_var.get() + "\n")
            self.textbox.insert(END, "FirstName\t\t" + self.First_var.get() + "\n")
            self.textbox.insert(END, "LastName\t\t" + self.Last_var.get() + "\n")
            self.textbox.insert(END, "address\t\t" + self.address_var.get() + "\n")
            self.textbox.insert(END, "Pin No\t\t" + self.pin_var.get() + "\n")
            self.textbox.insert(END, "mobile\t\t" + self.mobile_var.get() + "\n")
            self.textbox.insert(END, "BookID\t\t" + self.BookID_var.get() + "\n")
            self.textbox.insert(END, "BookTitle\t\t" + self.BookTitle_var.get() + "\n")
            self.textbox.insert(END, "Author\t\t" + self.Author_var.get() + "\n")
            self.textbox.insert(END, "DateBorrowed\t\t" + self.Date_Borrow_var.get() + "\n")
            self.textbox.insert(END, "DateDue\t\t" + self.DateDue_var.get() + "\n")
            self.textbox.insert(END, "DaysBook\t\t" + self.DaysBook_var.get() + "\n")
            self.textbox.insert(END, "LastReturnFine\t\t" + self.LastReturnFine_var.get() + "\n")
            self.textbox.insert(END, "DateOver\t\t" + self.DateOver_var.get() + "\n")

        def reset(self):
            self.member_var.set("")
            self.Prn_var.set("")
            self.ID_var.set("")
            self.First_var.set("")
            self.Last_var.set("")
            self.address_var.set("")
            self.pin_var.set("")
            self.mobile_var.set("")
            self.BookID_var.set("")
            self.BookTitle_var.set("")
            self.Author_var.set("")
            self.Date_Borrow_var.set("")
            self.DateDue_var.set("")
            self.DaysBook_var.set("")
            self.LastReturnFine_var.set("")
            self.DateOver_var.set("")
            self.textbox.delete("1.0", END)


        # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Label >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        lbl_title = Label(self.window, text="Library Management System", fg="white",
                          bg="black", bd=20, relief=RIDGE, padx=2, pady=6, font=("Times new Roman", 30, "bold"))
        lbl_title.pack(side=TOP, fill=X)
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Frame >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        frame = Frame(self.window, bg="black", relief=RIDGE, padx=20, bd=12)
        frame.place(x=0, y=99, width=1270, height=300)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< LeftFrame >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        LeftFrame = LabelFrame(self.window, text="LibraryManagementSystem", bg="black", fg="white", bd=5, relief=RIDGE,
                               font=("Times new roman", 10, "bold"))
        LeftFrame.place(x=10, y=110, width=700, height=280)

        lbl_member = Label(LeftFrame, text="Member Type", font=("Times new roman", 10, "bold"), padx=2, pady=6,
                           bg="black", fg="white")
        lbl_member.grid(row=0, column=0, sticky=W)

        type_member = ttk.Combobox(LeftFrame, font=("Times new roman", 10, "bold"), width=20, state="readonly",
                                   textvariable=self.member_var)
        type_member['value'] = ("Admin", "Student", "professor")
        type_member.grid(row=0, column=1)
# Parmenant Roll Number
        lbl_prn = Label(LeftFrame, text="PRN_NO:", font=("Times new roman", 10, "bold"), padx=2, pady=6,
                        bg="black", fg="white")
        lbl_prn.grid(row=1, column=0, sticky=W)

        txt_prn = Entry(LeftFrame, font=("Times new roman", 10, "bold"), width=23, textvariable=self.Prn_var)
        txt_prn.grid(row=1, column=1)

        lbl_id = Label(LeftFrame, text="ID NO:", font=("Times new roman", 10, "bold"), padx=2, pady=6,
                        bg="black", fg="white")
        lbl_id.grid(row=2, column=0, sticky=W)

        txt_id = Entry(LeftFrame, font=("Times new roman", 10, "bold"), width=23, textvariable=self.ID_var)
        txt_id.grid(row=2, column=1)

        lbl_Fn = Label(LeftFrame, text="FirstName:", font=("Times new roman", 10, "bold"), padx=2, pady=6,
                        bg="black", fg="white")
        lbl_Fn.grid(row=3, column=0, sticky=W)

        txt_Fn = Entry(LeftFrame, font=("Times new roman", 10, "bold"), width=23, textvariable=self.First_var)
        txt_Fn.grid(row=3, column=1)

        lbl_Ln = Label(LeftFrame, text="LastName:", font=("Times new roman", 10, "bold"), padx=2, pady=6,
                        bg="black", fg="white")
        lbl_Ln.grid(row=4, column=0, sticky=W)

        txt_Ln = Entry(LeftFrame, font=("Times new roman", 10, "bold"), width=23, textvariable=self.Last_var)
        txt_Ln.grid(row=4, column=1)

        lbl_Add = Label(LeftFrame, text="Address:", font=("Times new roman", 10, "bold"), padx=2, pady=6,
                        bg="black", fg="white")
        lbl_Add.grid(row=5, column=0, sticky=W)

        txt_Add= Entry(LeftFrame, font=("Times new roman", 10, "bold"), width=23, textvariable=self.address_var)
        txt_Add.grid(row=5, column=1)

        lbl_Pin = Label(LeftFrame, text="Pincode:", font=("Times new roman", 10, "bold"), padx=2, pady=6,
                        bg="black", fg="white")
        lbl_Pin.grid(row=6, column=0, sticky=W)

        txt_Pin= Entry(LeftFrame, font=("Times new roman", 10, "bold"), width=23, textvariable=self.pin_var)
        txt_Pin.grid(row=6, column=1)

        lbl_Phone = Label(LeftFrame, text="Mobile:", font=("Times new roman", 10, "bold"), padx=2, pady=6,
                        bg="black", fg="white")
        lbl_Phone.grid(row=7, column=0, sticky=W)

        txt_Phone= Entry(LeftFrame, font=("Times new roman", 10, "bold"), width=23, textvariable=self.mobile_var)
        txt_Phone.grid(row=7, column=1)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< column4 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        lbl_book_id = Label(LeftFrame, text="Book id:", font=("Times new roman", 10, "bold"), padx=2, pady=6,
                        bg="black", fg="white")
        lbl_book_id.grid(row=0, column=3, sticky=W)

        txt_Book_id= Entry(LeftFrame, font=("Times new roman", 10, "bold"), width=23, textvariable=self.BookID_var)
        txt_Book_id.grid(row=0, column=4)

        # -----

        lbl_book_title = Label(LeftFrame, text="Book Title:", font=("Times new roman", 10, "bold"), padx=2, pady=6,
                        bg="black", fg="white")
        lbl_book_title.grid(row=1, column=3, sticky=W)

        txt_Book_title= Entry(LeftFrame, font=("Times new roman", 10, "bold"), width=23, textvariable=self.BookTitle_var)
        txt_Book_title.grid(row=1, column=4)

# ----
        lbl_Authur = Label(LeftFrame, text="Author Name:", font=("Times new roman", 10, "bold"), padx=2, pady=6,
                        bg="black", fg="white")
        lbl_Authur.grid(row=2, column=3, sticky=W)

        txt_Auther= Entry(LeftFrame, font=("Times new roman", 10, "bold"), width=23, textvariable=self.Author_var)
        txt_Auther.grid(row=2, column=4)
# ---
        lbl_Date_Borrowed = Label(LeftFrame, text="Date Borrowed:", font=("Times new roman", 10, "bold"), padx=2,
                                  pady=6, bg="black", fg="white")
        lbl_Date_Borrowed.grid(row=3, column=3, sticky=W)

        txt_Date_Borrowed= Entry(LeftFrame, font=("Times new roman", 10, "bold"), width=23,
                                 textvariable=self.Date_Borrow_var)
        txt_Date_Borrowed.grid(row=3, column=4)
#  ---
        lbl_Date_Due = Label(LeftFrame, text="Date Due:", font=("Times new roman", 10, "bold"), padx=2,
                                  pady=6, bg="black", fg="white")
        lbl_Date_Due.grid(row=4, column=3, sticky=W)

        txt_Date_Due = Entry(LeftFrame, font=("Times new roman", 10, "bold"), width=23, textvariable=self.DateDue_var)
        txt_Date_Due.grid(row=4, column=4)

#  ----

        lbl_days_book = Label(LeftFrame, text="Days on Book:", font=("Times new roman", 10, "bold"), padx=2,
                                  pady=6, bg="black", fg="white")
        lbl_days_book.grid(row=5, column=3, sticky=W)

        txt_days_book = Entry(LeftFrame, font=("Times new roman", 10, "bold"), width=23, textvariable=self.DaysBook_var)
        txt_days_book.grid(row=5, column=4)

# ----------

        lbl_late_submit = Label(LeftFrame, text="Late return fine:", font=("Times new roman", 10, "bold"), padx=2,
                                  pady=6, bg="black", fg="white")
        lbl_late_submit.grid(row=6, column=3, sticky=W)

        txt_late_submit = Entry(LeftFrame, font=("Times new roman", 10, "bold"), width=23,
                                textvariable=self.LastReturnFine_var)
        txt_late_submit.grid(row=6, column=4)

# ------------------

        lbl_Date_over = Label(LeftFrame, text="Date over due:", font=("Times new roman", 10, "bold"), padx=2,
                                  pady=6, bg="black", fg="white")
        lbl_Date_over.grid(row=7, column=3, sticky=W)

        txt_Date_over = Entry(LeftFrame, font=("Times new roman", 10, "bold"), width=23, textvariable=self.DateOver_var)
        txt_Date_over.grid(row=7, column=4)
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< RightFrame >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        RightFrame = LabelFrame(self.window, text="Book Details", bg="black", fg="white", bd=5, relief=RIDGE,
                               font=("Times new roman", 10, "bold"))
        RightFrame.place(x=720, y=110, width=540, height=280)


# ------------------------

        self.textbox = Text(RightFrame, font=("Times new roman", 10, "bold"), width=36, height=16, padx=4, pady=6)
        self.textbox.grid(row=0, column=2)

        list_scrollbar = Scrollbar(RightFrame, orient="vertical")
        list_scrollbar.grid(row=0, column=1, sticky='ns')

        list_items = [
            "Head Firt Book", "Learn Python The Hard Way", "Python Programming", "Secrete Rahshy",
                   "Python CookBook", "Into to Machine Learning", "Fluent Pyt", "Machine tecno", "My Python",
                   "Joss Ellif guru", "Elite Jungle python", "Jungli Python", "Mumbai Python",
                   "Pune Python", "Machine python", "Advance Python", "Inton Python", "Red chlili phyton", "Ishq Python"
                   ]

        def select_book(event=""):
            value = str(listbox.get(listbox.curselection()))
            x = value

            if x == "Head Firt Book":
                self.BookID_var.set("BKid001")
                self.BookTitle_var.set("Python")
                self.Author_var.set("Edwin Charles")

                # Import the datetime module
                import datetime

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                # Convert datetime objects to string before setting
                self.Date_Borrow_var.set(d1.strftime("%Y-%m-%d %H:%M:%S"))
                self.DateDue_var.set(d3.strftime("%Y-%m-%d %H:%M:%S"))

                self.DaysBook_var.set(15)
                self.DateOver_var.set("NO")
                self.LastReturnFine_var.set("Rs.5")

            elif x == "Learn Python The Hard Way":
                self.BookID_var.set("BKid002")
                self.BookTitle_var.set("Python")
                self.Author_var.set("Edwin Charles")

                # Import the datetime module
                import datetime

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                    # Convert datetime objects to string before setting
                self.Date_Borrow_var.set(d1.strftime("%Y-%m-%d %H:%M:%S"))
                self.DateDue_var.set(d3.strftime("%Y-%m-%d %H:%M:%S"))

                self.DaysBook_var.set(15)
                self.DateOver_var.set("NO")
                self.LastReturnFine_var.set("Rs.5")

            elif x == "Python Programming":
                self.BookID_var.set("BKid001")
                self.BookTitle_var.set("Python")
                self.Author_var.set("Edwin Charles")

                    # Import the datetime module
                import datetime

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                # Convert datetime objects to string before setting
                self.Date_Borrow_var.set(d1.strftime("%Y-%m-%d %H:%M:%S"))
                self.DateDue_var.set(d3.strftime("%Y-%m-%d %H:%M:%S"))

                self.DaysBook_var.set(15)
                self.DateOver_var.set("NO")
                self.LastReturnFine_var.set("Rs.5")

            elif x == "Secrete Rahshy":
                self.BookID_var.set("BKid002")
                self.BookTitle_var.set("Python")
                self.Author_var.set("Edwin Charles")

                # Import the datetime module
                import datetime

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                    # Convert datetime objects to string before setting
                self.Date_Borrow_var.set(d1.strftime("%Y-%m-%d %H:%M:%S"))
                self.DateDue_var.set(d3.strftime("%Y-%m-%d %H:%M:%S"))

                self.DaysBook_var.set(15)
                self.DateOver_var.set("NO")
                self.LastReturnFine_var.set("Rs.5")

            elif x == "Python CookBook":
                self.BookID_var.set("BKid002")
                self.BookTitle_var.set("Python")
                self.Author_var.set("Edwin Charles")

                # Import the datetime module
                import datetime

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                    # Convert datetime objects to string before setting
                self.Date_Borrow_var.set(d1.strftime("%Y-%m-%d %H:%M:%S"))
                self.DateDue_var.set(d3.strftime("%Y-%m-%d %H:%M:%S"))

                self.DaysBook_var.set(15)
                self.DateOver_var.set("NO")
                self.LastReturnFine_var.set("Rs.5")

            elif x == "Into to Machine Learning":
                self.BookID_var.set("BKid002")
                self.BookTitle_var.set("Python")
                self.Author_var.set("Edwin Charles")

                # Import the datetime module
                import datetime

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                    # Convert datetime objects to string before setting
                self.Date_Borrow_var.set(d1.strftime("%Y-%m-%d %H:%M:%S"))
                self.DateDue_var.set(d3.strftime("%Y-%m-%d %H:%M:%S"))

                self.DaysBook_var.set(15)
                self.DateOver_var.set("NO")
                self.LastReturnFine_var.set("Rs.5")

            elif x == "Fluent Pyt":
                self.BookID_var.set("BKid002")
                self.BookTitle_var.set("Python")
                self.Author_var.set("Edwin Charles")

                # Import the datetime module
                import datetime

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                    # Convert datetime objects to string before setting
                self.Date_Borrow_var.set(d1.strftime("%Y-%m-%d %H:%M:%S"))
                self.DateDue_var.set(d3.strftime("%Y-%m-%d %H:%M:%S"))

                self.DaysBook_var.set(15)
                self.DateOver_var.set("NO")
                self.LastReturnFine_var.set("Rs.5")

            elif x == "Machine tecno":
                self.BookID_var.set("BKid002")
                self.BookTitle_var.set("Python")
                self.Author_var.set("Edwin Charles")

                # Import the datetime module
                import datetime

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                    # Convert datetime objects to string before setting
                self.Date_Borrow_var.set(d1.strftime("%Y-%m-%d %H:%M:%S"))
                self.DateDue_var.set(d3.strftime("%Y-%m-%d %H:%M:%S"))

                self.DaysBook_var.set(15)
                self.DateOver_var.set("NO")
                self.LastReturnFine_var.set("Rs.5")

            elif x == "My Python":
                self.BookID_var.set("BKid002")
                self.BookTitle_var.set("Python")
                self.Author_var.set("Edwin Charles")

                # Import the datetime module
                import datetime

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                    # Convert datetime objects to string before setting
                self.Date_Borrow_var.set(d1.strftime("%Y-%m-%d %H:%M:%S"))
                self.DateDue_var.set(d3.strftime("%Y-%m-%d %H:%M:%S"))

                self.DaysBook_var.set(15)
                self.DateOver_var.set("NO")
                self.LastReturnFine_var.set("Rs.5")

            elif x == "Joss Ellif guru":
                self.BookID_var.set("BKid002")
                self.BookTitle_var.set("Python")
                self.Author_var.set("Edwin Charles")

                # Import the datetime module
                import datetime

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                    # Convert datetime objects to string before setting
                self.Date_Borrow_var.set(d1.strftime("%Y-%m-%d %H:%M:%S"))
                self.DateDue_var.set(d3.strftime("%Y-%m-%d %H:%M:%S"))

                self.DaysBook_var.set(15)
                self.DateOver_var.set("NO")
                self.LastReturnFine_var.set("Rs.5")

            elif x == "Elite Jungle python":
                self.BookID_var.set("BKid002")
                self.BookTitle_var.set("Python")
                self.Author_var.set("Edwin Charles")

                # Import the datetime module
                import datetime

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                    # Convert datetime objects to string before setting
                self.Date_Borrow_var.set(d1.strftime("%Y-%m-%d %H:%M:%S"))
                self.DateDue_var.set(d3.strftime("%Y-%m-%d %H:%M:%S"))

                self.DaysBook_var.set(15)
                self.DateOver_var.set("NO")
                self.LastReturnFine_var.set("Rs.5")

            elif x == "Jungli Python":
                self.BookID_var.set("BKid002")
                self.BookTitle_var.set("Python")
                self.Author_var.set("Edwin Charles")

                # Import the datetime module
                import datetime

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                    # Convert datetime objects to string before setting
                self.Date_Borrow_var.set(d1.strftime("%Y-%m-%d %H:%M:%S"))
                self.DateDue_var.set(d3.strftime("%Y-%m-%d %H:%M:%S"))

                self.DaysBook_var.set(15)
                self.DateOver_var.set("NO")
                self.LastReturnFine_var.set("Rs.5")

            elif x == "Mumbai Python":
                self.BookID_var.set("BKid002")
                self.BookTitle_var.set("Python")
                self.Author_var.set("Edwin Charles")

                # Import the datetime module
                import datetime

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                    # Convert datetime objects to string before setting
                self.Date_Borrow_var.set(d1.strftime("%Y-%m-%d %H:%M:%S"))
                self.DateDue_var.set(d3.strftime("%Y-%m-%d %H:%M:%S"))

                self.DaysBook_var.set(15)
                self.DateOver_var.set("NO")
                self.LastReturnFine_var.set("Rs.5")

            elif x == "Pune Python":
                self.BookID_var.set("BKid002")
                self.BookTitle_var.set("Python")
                self.Author_var.set("Edwin Charles")

                # Import the datetime module
                import datetime

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                    # Convert datetime objects to string before setting
                self.Date_Borrow_var.set(d1.strftime("%Y-%m-%d %H:%M:%S"))
                self.DateDue_var.set(d3.strftime("%Y-%m-%d %H:%M:%S"))

                self.DaysBook_var.set(15)
                self.DateOver_var.set("NO")
                self.LastReturnFine_var.set("Rs.5")

            elif x == "Machine Python":
                self.BookID_var.set("BKid002")
                self.BookTitle_var.set("Python")
                self.Author_var.set("Edwin Charles")

                # Import the datetime module
                import datetime

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                    # Convert datetime objects to string before setting
                self.Date_Borrow_var.set(d1.strftime("%Y-%m-%d %H:%M:%S"))
                self.DateDue_var.set(d3.strftime("%Y-%m-%d %H:%M:%S"))

                self.DaysBook_var.set(15)
                self.DateOver_var.set("NO")
                self.LastReturnFine_var.set("Rs.5")

            elif x == "Advance Python":
                self.BookID_var.set("BKid002")
                self.BookTitle_var.set("Python")
                self.Author_var.set("Edwin Charles")

                # Import the datetime module
                import datetime

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                    # Convert datetime objects to string before setting
                self.Date_Borrow_var.set(d1.strftime("%Y-%m-%d %H:%M:%S"))
                self.DateDue_var.set(d3.strftime("%Y-%m-%d %H:%M:%S"))

                self.DaysBook_var.set(15)
                self.DateOver_var.set("NO")
                self.LastReturnFine_var.set("Rs.5")

            elif x == "Inton Python":
                self.BookID_var.set("BKid002")
                self.BookTitle_var.set("Python")
                self.Author_var.set("Edwin Charles")

                # Import the datetime module
                import datetime

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                    # Convert datetime objects to string before setting
                self.Date_Borrow_var.set(d1.strftime("%Y-%m-%d %H:%M:%S"))
                self.DateDue_var.set(d3.strftime("%Y-%m-%d %H:%M:%S"))

                self.DaysBook_var.set(15)
                self.DateOver_var.set("NO")
                self.LastReturnFine_var.set("Rs.5")

            elif x == "RedChilli Python":
                self.BookID_var.set("BKid002")
                self.BookTitle_var.set("Python")
                self.Author_var.set("Edwin Charles")

                # Import the datetime module
                import datetime

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                    # Convert datetime objects to string before setting
                self.Date_Borrow_var.set(d1.strftime("%Y-%m-%d %H:%M:%S"))
                self.DateDue_var.set(d3.strftime("%Y-%m-%d %H:%M:%S"))

                self.DaysBook_var.set(15)
                self.DateOver_var.set("NO")
                self.LastReturnFine_var.set("Rs.5")

            elif x == "Ishq Python":
                self.BookID_var.set("BKid002")
                self.BookTitle_var.set("Python")
                self.Author_var.set("Edwin Charles")

                # Import the datetime module
                import datetime

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                    # Convert datetime objects to string before setting
                self.Date_Borrow_var.set(d1.strftime("%Y-%m-%d %H:%M:%S"))
                self.DateDue_var.set(d3.strftime("%Y-%m-%d %H:%M:%S"))

                self.DaysBook_var.set(15)
                self.DateOver_var.set("NO")
                self.LastReturnFine_var.set("Rs.5")

        # Create Listbox and bind the event
        listbox = Listbox(RightFrame, font=("Times new roman", 10, "bold"), width=30, height=16)
        listbox.bind("<<ListboxSelect>>", select_book)
        listbox.grid(row=0, column=0, padx=10)

        list_scrollbar.config(command=listbox.yview)

        for items in list_items:
            listbox.insert(END, items)

        def adda_data(self):
            con = mysql.connector.connect(host="localhost", username="root", password="Root", database="collage")
            my_cursor = con.cursor()
            my_cursor.execute("insert into collage values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                              (self.member_var.get(),
                               self.Prn_var.get(),
                               self.ID_var.get(),
                               self.First_var.get(),
                               self.Last_var.get(),
                               self.address_var.get(),
                               self.pin_var.get(),
                               self.mobile_var.get(),
                               self.BookID_var.get(),
                               self.BookTitle_var.get(),
                               self.Author_var.get(),
                               self.Date_Borrow_var.get(),
                               self.DateDue_var.get(),
                               self.DaysBook_var.get(),
                               self.LastReturnFine_var.get(),
                               self.DateOver_var.get()))
            con.commit()
            self.fetch_data()
            con.close()

            messagebox.showinfo("Succeed", "data saved successfully")

        # Correct indentation for fetch_data method
        def fetch_data(self):
            con = mysql.connector.connect(host="localhost", username="root", password="Root", database="collage")
            my_cursor = con.cursor()
            my_cursor.execute("select * from library")
            rows = my_cursor.fetchall()

            if len(rows) != 0:
                self.library_table.delete(*self.library_table.get_children())
                for i in rows:
                    self.library_table.insert("", END, values=i)
                con.commit()
            con.close()

        def exit(self):
            do = messagebox.askyesno("LMS", "Do you want to exit")
            if do > 0:
                quit()

        def update(self):
            con = mysql.connector.connect(host="localhost", username="root", password="Root", database="collage")
            my_cursor = con.cursor()
            my_cursor.execute("update into collage values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                              (self.member_var.get(),
                               self.Prn_var.get(),
                               self.ID_var.get(),
                               self.First_var.get(),
                               self.Last_var.get(),
                               self.address_var.get(),
                               self.pin_var.get(),
                               self.mobile_var.get(),
                               self.BookID_var.get(),
                               self.BookTitle_var.get(),
                               self.Author_var.get(),
                               self.Date_Borrow_var.get(),
                               self.DateDue_var.get(),
                               self.DaysBook_var.get(),
                               self.LastReturnFine_var.get(),
                               self.DateOver_var.get()))
            con.commit()
            self.fetch_data()
            con.close()

        def deleted(self):
            if self.prn_var.get() =="" or self.id_var.get() == "":
                messagebox.showerror("Error", "Please fill the fields")
            else:
                con = mysql.connector.connect(host="localhost", username="root", password="Root",
                                                  database="collage")
                my_cursor = con.cursor()
                query = "delete from collage where Prn_no=%s"
                value = (self.prn_var.get(),)
                my_cursor.execute(query, value)

                con.commit()
                fetch_data()
                reset()
                con.close()

                messagebox.showinfo("success,", "member has been deleted")


        # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Buttons >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        button_frame = Frame(self.window, bg="black", relief=RIDGE, padx=20, bd=12)
        button_frame.place(x=0, y=400, width=1270, height=60)

        btn_add_data = Button(button_frame, text="Add Data", font=("Times new roman", 10, "bold"), width=27, bg="blue",
                              fg="white", pady=5, command=adda_data)
        btn_add_data.grid(row=0, column=0)

        btn_show_data = Button(button_frame, command=showdata, text="Show Data", font=("Times new roman", 10, "bold"), width=27, bg="blue",
                              fg="white", pady=5)
        btn_show_data.grid(row=0, column=1)

        btn_Update_data = Button(button_frame, command=update, text="Update", font=("Times new roman", 10, "bold"), width=27, bg="blue",
                              fg="white", pady=5)
        btn_Update_data.grid(row=0, column=2)

        btn_Delete_data = Button(button_frame, command=deleted, text="Delete", font=("Times new roman", 10, "bold"), width=27, bg="blue",
                              fg="white", pady=5)
        btn_Delete_data.grid(row=0, column=3)

        btn_Reset_data = Button(button_frame, command=reset, text="Reset", font=("Times new roman", 10, "bold"), width=27, bg="blue",
                              fg="white", pady=5)
        btn_Reset_data.grid(row=0, column=4)

        btn_exit = Button(button_frame, command=exit, text="Exit", font=("Times new roman", 10, "bold"), width=27, bg="blue",
                              fg="white", pady=5)
        btn_exit.grid(row=0, column=5)


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Mysql server viewer >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        Info_frame = Frame(self.window, bg="black", relief=RIDGE, padx=10, bd=12)
        Info_frame.place(x=0, y=461, width=1270, height=180)

        table_frame = Frame(Info_frame, bg="black", relief=RIDGE, bd=8)
        table_frame.place(x=0, y=1, width=1230, height=160)

        xscroll = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.library_table = ttk.Treeview(table_frame, columns=("MemberType", "PrnNO", "IdNo", "Firstname",
                                                                "Lastname", "Address", "PinCode", "Mobile",
                                                                "BookId", "BookTitle", "AuthorName",
                                                                "DateBorrowed", "DateDue", "DateOfBook",
                                                                "LateReturnFine", "DateOverDue"),
                                          xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        self.library_table.heading("MemberType", text="Member Type")
        self.library_table.heading("PrnNO", text="PRN NO")
        self.library_table.heading("IdNo", text="Id No")
        self.library_table.heading("Firstname", text="First Name")
        self.library_table.heading("Lastname", text="Last Name")
        self.library_table.heading("Address", text="Address")
        self.library_table.heading("PinCode", text="Pin Code")
        self.library_table.heading("Mobile", text="Mobile No")
        self.library_table.heading("BookId", text="Book Id")
        self.library_table.heading("BookTitle", text="Book Title")
        self.library_table.heading("AuthorName", text="Author Name")
        self.library_table.heading("DateBorrowed", text="Date Borrowed")
        self.library_table.heading("DateDue", text="Date Due")
        self.library_table.heading("DateOfBook", text="Date Of Book")
        self.library_table.heading("LateReturnFine", text="Late Return Fine")
        self.library_table.heading("DateOverDue", text="Date Over Due")

        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH, expand=1)

        self.library_table.column("MemberType", width=100)
        self.library_table.column("PrnNO", width=100)
        self.library_table.column("IdNo", width=100)
        self.library_table.column("Firstname", width=100)
        self.library_table.column("Lastname", width=100)
        self.library_table.column("Address", width=100)
        self.library_table.column("PinCode", width=100)
        self.library_table.column("Mobile", width=100)
        self.library_table.column("BookId", width=100)
        self.library_table.column("BookTitle", width=100)
        self.library_table.column("AuthorName", width=100)
        self.library_table.column("DateBorrowed", width=100)
        self.library_table.column("DateDue", width=100)
        self.library_table.column("DateOfBook", width=100)
        self.library_table.column("LateReturnFine", width=100)
        self.library_table.column("DateOverDue", width=100)

        def get_cursur(event):
            cursor_row = self.library_table.focus()
            content = self.library_table.item(cursor_row)
            row = content['values']

            self.member_var.set(row[0])
            self.Prn_var.set(row[1])
            self.ID_var.set(row[2])
            self.First_var.set(row[3])
            self.Last_var.set(row[4])
            self.address_var.set(row[5])
            self.pin_var.set(row[6])
            self.mobile_var.set(row[7])
            self.BookID_var.set(row[8])
            self.BookTitle_var.set(row[9])
            self.Author_var.set(row[10])
            self.Date_Borrow_var.set(row[11])
            self.DateDue_var.set(row[12])
            self.DaysBook_var.set(row[13])
            self.LastReturnFine_var.set(row[14])
            self.DateOver_var.set(row[15])



        self.library_table.bind("<ButtonRelease-1>", get_cursur)



if __name__ == "__main__":
    window = Tk()
    obj = LibraryManagementSystem(window)
    window.mainloop()