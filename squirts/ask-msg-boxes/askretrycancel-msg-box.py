"""askretrycancel msg box.
   Stand-alone example from Tk Assistant.
   stevepython.wordpress.com
"""

from tkinter import messagebox, Tk

root = Tk()
root.withdraw() # Remove annoying window.

ask_rc = messagebox.askretrycancel('Question',
                                   'This is a Retry Cancel message box.')

if ask_rc:
    print('You clicked on Retry')
else:
    print('You clicked cancel')
