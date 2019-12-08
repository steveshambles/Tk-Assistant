"""Info message box.
   Stand-alone example from Tk Assistant.
   stevepython.wordpress.com"""

from tkinter import messagebox, Tk

root = Tk()
root.withdraw()

messagebox.showinfo('Info', 'This is a info message box.')
