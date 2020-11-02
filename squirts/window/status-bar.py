"""Status bar.
   Stand-alone example from Tk Assistant.
   stevepython.wordpress.com
   pyshambles.blogspot.com
   """
from tkinter import BOTTOM, Label, SUNKEN, Tk, W, X

root = Tk()
root.title('Status bar example')
root.geometry('300x150')

st_bar = Label(root, text='Status: Ready', bd=1, relief=SUNKEN, anchor=W)
st_bar.pack(side=BOTTOM, fill=X)

root.mainloop()
