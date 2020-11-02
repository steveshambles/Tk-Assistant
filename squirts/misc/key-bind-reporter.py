"""Key bind reporter.
Stand-alone example from Tk Assistant.
stevepython..wordpress.com
pyshambles.blogspot.com
"""
from tkinter import messagebox, Tk

def key_press(evt):
    print('key detected\n',evt)
    messagebox.showinfo('key detected\n', evt)

root = Tk()
root.title("Press any key")
root.geometry('230x200')
root.bind("<Key>", key_press)

root.mainloop()
