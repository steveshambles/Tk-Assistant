"""Simple Label.
Stand-alone code from Tk Assistant.
stevepython.wordpress.com
pyshambles.blogspot.com
"""
from tkinter import Label, Tk

root = Tk()
root.title('Simple label example')

txt_label = Label(root, bg='plum',
                  text='This is text on a simple label with a plum bg colour.')
txt_label.grid()

root.mainloop()
