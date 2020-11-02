"""User input dialog.
   Stand-alone example from Tk Assistant.
   stevepython.wordpress.com
   pyshambles.blogspot.com
"""
from tkinter import simpledialog, Tk

root = Tk()
root.withdraw()

user_input = simpledialog.askstring(title='Test input dialog',
                                    prompt='What is your name?:')

print('Hello', user_input)

root.mainloop()
