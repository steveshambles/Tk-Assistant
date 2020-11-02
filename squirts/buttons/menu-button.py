"""Menu button
   Stand-alone example from Tk Assistant.
   stevepython.wordpress.com
   pyshambles.blogspot.com
"""
from tkinter import IntVar, Menu, Menubutton, Tk

root = Tk()
root.title('Menu button example')

def menu_sel():
    """Check and report on menu selection."""
    if VAR1.get():
        print('V2 ticked')
    if VAR2.get():
        print('V3 ticked')

menu_btn = Menubutton(root, text='Choose Python Version', bg='skyblue')
menu_btn.grid(padx=20, pady=20)

menu_btn.menu = Menu(menu_btn, tearoff=0)
menu_btn['menu'] = menu_btn.menu

VAR1 = IntVar()
VAR2 = IntVar()

menu_btn.menu.add_checkbutton(label='Python V2',
                              variable=VAR1, command=menu_sel)
menu_btn.menu.add_checkbutton(label='Python V3',
                              variable=VAR2, command=menu_sel)
menu_btn.grid()

root.mainloop()
