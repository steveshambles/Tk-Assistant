"""askokcancel msg box.
   Stand-alone example from Tk Assistant.
   stevepython.wordpress.com
   pyshambles.blogspot.com
"""
from tkinter import messagebox, Tk

root = Tk()
root.withdraw() # Remove annoying window.

ask_okc = messagebox.askokcancel('Question',
                                 'This is a OK-Cancel message box.')

if ask_okc:
    print('You clicked on OK')

else:
    print('You clicked cancel')
