"""Paned Windows.
   Stand-alone example from Tk Assistant.
   stevepython.wordpress.com"""

from tkinter import BOTH, Label, PanedWindow, Tk, VERTICAL

root = Tk()
root.title('PanedWindow Example')

m1 = PanedWindow(showhandle=True)
m1.pack(fill=BOTH, expand=1)

left_pane = Label(m1, bg='skyblue', text='Left PanedWindow',
                  relief='sunken', bd=4)
m1.add(left_pane)

m2 = PanedWindow(m1, orient=VERTICAL, showhandle=True)
m1.add(m2)

top_pane = Label(m2, bg='red', text='Top PanedWindow',
                 relief='sunken', bd=4)
m2.add(top_pane)

btm_pane = Label(m2, bg='gold', text='Bottom PanedWindow',
                 relief='sunken', bd=4)
m2.add(btm_pane)

root.mainloop()
