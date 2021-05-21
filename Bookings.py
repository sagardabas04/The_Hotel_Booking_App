from tkinter import *
from tkinter import ttk
import pandas as pd

def bookingsButton():    
    df = pd.read_csv("Bookings.csv")
    records = df.values.tolist()

    window1 = Tk()
    window1.title("All Bookings")
    window1.geometry('1000x500')
    window1.configure(background = "black")

    frm = Frame(window1)
    frm.pack()

    tv = ttk.Treeview(frm, columns = (1, 2, 3, 4, 5), show = 'headings', height = '5')
    tv.pack()

    tv.heading(1, text = "Name")
    tv.heading(2, text = "Phone Number")
    tv.heading(3, text = "Room Number")
    tv.heading(4, text = "Check In Date")
    tv.heading(5, text = "No. of days of stay")

    for i in records:
        tv.insert('', 'end', values = i)

    window1.mainloop()

