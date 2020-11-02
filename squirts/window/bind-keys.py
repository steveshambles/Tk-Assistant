"""Bind keys to a window.
Stand-alone example from Tk Assistant.
stevepython.wordpress.com
pyshambles.blogspot.com
"""
from tkinter import Label, messagebox, Tk

root = Tk()
root.title('Bind keys to a window example')
root.geometry('330x260')

start = Label(root, bg='powderblue',
              text='\n\nTry pressing:\n\nq\nDouble enter\nAlt-Enter\nCtrl-c\n'
              'spacebar\nEscape\nF1\nLeft Shift x\nRight shift F2\nWin key\n\n')
start.grid()

def key_catch(txt):
    """Outputs message in a pop up.
       txt = your message to print in msgbox."""
    messagebox.showinfo('Key detected', 'You pressed.\n\n'+txt)

# A few keypress examples.
root.bind('<Double-Return>', lambda event: key_catch('Double Enter'))
root.bind('<Alt_L><Return>', lambda event: key_catch('Alt-Enter'))
root.bind('<Control-c>', lambda event: key_catch('Control c'))
root.bind('<q>', lambda event: key_catch('q'))
root.bind('<space>', lambda event: key_catch('Spacebar'))
root.bind('<Escape>', lambda event: key_catch('Escape'))
root.bind('<F1>', lambda event: key_catch('F1'))
root.bind('<Shift_L><X>', lambda event: key_catch('Left shift x'))
root.bind('<Shift_R><F2>', lambda event: key_catch('Right shift F2'))
root.bind('<Win_L>', lambda event: key_catch('Windows key'))

root.mainloop()
