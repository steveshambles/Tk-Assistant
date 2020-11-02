"""Spinbox.
   Stand-alone example from Tk Assistant.
   stevepython.wordpress.com
   https://pyshambles.blogspot.com/
   """
from tkinter import Button, IntVar, LabelFrame, messagebox, Spinbox
from tkinter import TclError, Tk

root = Tk()
root.title('Spinbox example')
root.resizable(False,False)

def spbox_val():
    """Display spinbox current value."""
    # If input is invalid, eg.non-numeric or blank, then return.
    try:
        spnbx_val = VAR.get()
    except TclError:
        return

    messagebox.showinfo('Spinbox', 'Spinbox value is '+str(spnbx_val))

main_frame = LabelFrame(root, fg='blue', text='  Spinbox  ')
main_frame.grid(padx=10, pady=13, ipadx=5, ipady=3)

VAR = IntVar()
VAR.set(50)

spn_bx = Spinbox(main_frame, from_=0, to=100, width=4, textvariable=VAR)

Button(main_frame, bg='green2', text='Spinbox value',
       command=spbox_val).grid(row=0, column=1)

spn_bx.grid(column=0, row=0, padx=10, pady=10)

root.mainloop()
