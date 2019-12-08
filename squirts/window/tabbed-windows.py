"""Tabbed GUI.
   Stand-alone example from Tk Assistant.
   stevepython.wordpress.com"""

from tkinter import Tk
from tkinter import ttk

root = Tk()
root.title('Tabbed GUI example')

tab_ctrl = ttk.Notebook(root)

tab_one = ttk.Frame(tab_ctrl)
tab_ctrl.add(tab_one, text='Tab 1')

tab_two = ttk.Frame(tab_ctrl)
tab_ctrl.add(tab_two, text='Tab 2')
tab_ctrl.pack(expand=1, fill='both')

ttk.Label(tab_one, text='This is Tab 1').grid(column=0,
                                              row=0, padx=10, pady=10)
ttk.Label(tab_two, text='This is Tab 2').grid(column=0,
                                              row=0, padx=10, pady=10)

root.mainloop()
