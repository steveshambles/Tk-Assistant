"""Progress bar.
Stand-alone code from Tk Assistant..
stevepython.wordpress.com
pyshambles.blogspot.com
"""
from tkinter import Button, HORIZONTAL, Label, Tk
from tkinter.ttk import Progressbar
import time

root = Tk()
root.title('Progress Bar')
root.geometry('200x45')

def prg_bar():
    """Move the progress bar"""
    pro_gress = 1
    while pro_gress < 101:
        prog_bar['value'] = pro_gress
        root.update_idletasks()
        time.sleep(0.1)
        pro_label = Label(root, text=str(pro_gress)+'%')
        pro_label.grid(row=1, column=2)
        pro_gress += 1
        root.update_idletasks()

prog_bar = Progressbar(root, orient=HORIZONTAL, length=100,
                       mode='determinate')
prog_bar.grid(row=1, column=1)

Button(root, text='Go', bg='limegreen',
       command=prg_bar).grid(padx=10, pady=10, row=1, column=0)

int_label = Label(root, text='%')
int_label.grid(row=1, column=2)

root.mainloop()
