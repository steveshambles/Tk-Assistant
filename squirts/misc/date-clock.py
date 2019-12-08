""" Date and ticking clock.
Stand-alone example from Tk Assistant.

By Steve Shambles
stevepython..wordpress.com
"""
from threading import Timer
import time
from tkinter import Label, Tk

root = Tk()
root.title('Date and Clock Example')

# Create label for clock.
date_clock = Label(root, bg='skyblue')
date_clock.grid(row=2, column=1, padx=20)

def date_time():
    """Threading timer prints date and time every second."""
    curr_time = (time.strftime("%a %b %Y  %H:%M:%S", time.gmtime()))
    date_clock.config(text=curr_time) # Print updated clock.
    t = Timer(1.0, date_time)
    t.start()

# Starts the timer.
date_time()

root.mainloop()
