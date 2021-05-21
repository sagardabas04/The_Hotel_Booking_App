from tkinter import *
from tkinter import ttk
import login
import Checkin

def bookingsButton():
    login.loginscreen()

def checkIn():
    Checkin.checkin()

window = Tk()
window.title("Booking Window")
window.geometry("1000x600")
window.configure(background = "black")

Label(window, text = 'Click to See Bookings(Staff only): ', bg = "black", fg = 'white', font = "arial 12 bold").grid(row = 0, column = 0, sticky = W)
Button(window, text = 'Show All Bookings', width = 17, command = bookingsButton).grid(row = 1, column = 0, sticky = W)

def close_window():
    window.destroy()
    exit()

Label(window, text = 'Click to exit: ', bg = "black", fg = 'white', font = "arial 12 bold").grid(row = 2, column = 0, sticky = W)
Button(window, text = 'Exit', width = 14, command = close_window).grid(row = 3, column = 0, sticky = W)

Label(window, text = 'Click to Check in: ', bg = "black", fg = 'white', font = "arial 12 bold").grid(row = 0, column = 2, sticky = W)
Button(window, text = 'Check In', width = 14, command = checkIn).grid(row = 1, column = 2, sticky = W)

window.mainloop()
