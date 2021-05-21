from tkinter import *
import Bookings
from tkinter import messagebox

def loginscreen():
    username = "a"
    password = "a"

    def close_window():
        window2.destroy()
    
    def click():
        entered_text1 = a.get()
        entered_text2 = b.get()
        if username == entered_text1 and password == entered_text2:
            close_window()
            Bookings.bookingsButton()
            
        else:
            messagebox.showerror("Error", "Invalid Username/Password")

    window2 = Tk()
    window2.title("Login to look at all the bookings")
    window2.geometry("300x200")
    window2.configure(background = "black")

    Label(window2, text = 'Username', bg = "black", fg = 'white', font = "arial 12 bold").grid(row = 2, column = 0, sticky = W)
    a = Entry(window2, width = 20, bg = "White")
    a.grid(row = 3, column = 0, sticky = W)

    Label(window2, text = 'Password', bg = "black", fg = 'white', font = "arial 12 bold").grid(row = 5, column = 0, sticky = W)
    b = Entry(window2, width = 20, bg = "White")
    b.grid(row = 6, column = 0, sticky = W)

    Button(window2, text = 'Submit', cursor = "hand2", width = 6, command = click).grid(row = 7, column = 0, sticky = W)

    window2.mainloop()
