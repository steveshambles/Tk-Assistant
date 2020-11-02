"""Warning message box.
   Stand-alone example from Tk Assistant.
   stevepython.wordpress.com
   pyshambles.blogspot.com
"""
from tkinter import messagebox, Tk

root = Tk()
root.withdraw()

messagebox.showwarning('Warning', 'This is a warning message box.')
