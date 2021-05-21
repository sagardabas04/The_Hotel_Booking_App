from tkinter import *
from tkinter import ttk
import pandas as pd
import csv

def checkin():
    def close_window():
        window.destroy()

    def click():
        name = a.get()
        phone = b.get()
        room = c.get()
        checkindate = d.get()
        days = e.get()
        temp = [name, phone, room, checkindate, days]
        bookedRooms = []

        with open("Bookings.csv","r") as f:
            reader = csv.reader(f,delimiter = ",")
            data = list(reader)
            row_count = len(data)
        
        csvfile = open('Bookings.csv','r')
        csvFileArray = []

        for row in csv.reader(csvfile):
            csvFileArray.append(row)

        for i in range(1, row_count-1):
            bookedRooms.append(csvFileArray[i][2])

        for i in bookedRooms:
            if i == room:
                output.delete(0.0, END)
                output.insert(END, name + " This room is already booked please check another room")
                break
        else:
            with open("Bookings.csv", 'a+', newline='') as write_obj:
                csv_writer = csv.writer(write_obj)
                csv_writer.writerow(temp)
            output.delete(0.0, END)
            output.insert(END, name + " Booking Confirmed! Please pay at the counter.")

    window = Tk()
    window.title("Check in")
    window.configure(background = "black")

    Label(window, text = 'Enter Name: ', bg = "black", fg = 'white', font = "arial 12 bold").grid(row = 1, column = 0, sticky = W)
    a = Entry(window, width = 20, bg = "White")
    a.grid(row = 2, column = 0, sticky = W)

    Label(window, text = 'Phone Number: ', bg = "black", fg = 'white', font = "arial 12 bold").grid(row = 3, column = 0, sticky = W)
    b = Entry(window, width = 20, bg = "White")
    b.grid(row = 4, column = 0, sticky = W)

    Label(window, text = 'Enter Room number: ', bg = "black", fg = 'white', font = "arial 12 bold").grid(row = 5, column = 0, sticky = W)
    c = Entry(window, width = 20, bg = "White")
    c.grid(row = 6, column = 0, sticky = W)

    Label(window, text = 'Check In Date: ', bg = "black", fg = 'white', font = "arial 12 bold").grid(row = 7, column = 0, sticky = W)
    d = Entry(window, width = 20, bg = "White")
    d.grid(row = 8, column = 0, sticky = W)

    Label(window, text = 'No. of days of stay: ', bg = "black", fg = 'white', font = "arial 12 bold").grid(row = 9, column = 0, sticky = W)
    e = Entry(window, width = 20, bg = "White")
    e.grid(row = 10, column = 0, sticky = W)

    Button(window, text = 'Submit', width = 6, command = click).grid(row = 11, column = 0, sticky = W)

    output = Text(window, width = 100, height = 1,wrap = WORD, background = "white")
    output.grid(row = 12, column = 0, sticky = W)

    window.mainloop()
