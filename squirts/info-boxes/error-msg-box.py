"""Error message box.
   Stand-alone example from Tk Assistant.
   stevepython.wordpress.com"""

from tkinter import messagebox, Tk

root = Tk()
root.withdraw()

messagebox.showerror('Error', 'This is a error message box.')
