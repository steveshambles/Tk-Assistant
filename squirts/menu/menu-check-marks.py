"""Menu check-mark.
   Stand-alone example by Tk Assistant.
   stevepython.wordpress.com"""

from tkinter import IntVar, Menu, Tk

root = Tk()
root.title('Menu check-mark example')

def use_clean_insults():
    """When clean insults selected set cleanvar."""
    cleanVar.set(1)
    rudeVar.set(0)
    print('Clean insults selected')

def use_rude_insults():
    """When clean insults selected unset cleanvar."""
    cleanVar.set(0)
    rudeVar.set(1)
    print('Rude insults selected')

# Set vars up menu check.
cleanVar = IntVar()
cleanVar.set(1) # Start off as default menu option.

rudeVar = IntVar()
rudeVar.set(0)

# Set up drop-down menu.
menu_bar = Menu(root)
insults_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Insults", menu=insults_menu)

insults_menu.add_checkbutton(label="Use Clean Insults",
                             variable=cleanVar, command=use_clean_insults)

insults_menu.add_checkbutton(label="Use Rude Insults",
                             variable=rudeVar, command=use_rude_insults)

insults_menu.add_checkbutton(label="Exit",
                             command=root.destroy)
root.config(menu=menu_bar)

root.mainloop()
