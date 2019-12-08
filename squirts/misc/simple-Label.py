"""Simple Label.
   Stand-alone code from Tk Assistant.
   stevepython.wordpress.com"""

from tkinter import Label, Tk

root = Tk()
root.title('Simple Label example')

txt_label = Label(root, bg='plum',
                  text='This is text on a simple label')
txt_label.grid()

root.mainloop()
