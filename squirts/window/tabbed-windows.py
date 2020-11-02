"""Tabbed GUI.
Stand-alone example from Tk Assistant.
stevepython.wordpress.com
pyshambles.blogspot.com
"""
import time
from tkinter import INSERT, Text, Tk, WORD
from tkinter import ttk
import pyperclip

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

text = Text(tab_one, height=10, width=60)
text.grid()

text.config(background='steelblue', foreground='white')

def view_cb():
    """Get current clipboard contents."""
    # Get current clipboard contents.
    cb_get = pyperclip.paste()
    # Set length of title bar and the character to use.
    tit_bar = '-' *5
    text.config(wrap=WORD)
    curr_time = time.asctime()
    # Insert clipboard text into text box with time and date stamp.
    text.insert(INSERT,
                '\n'+tit_bar+'Clipboard contents at: '
                +curr_time+' '+tit_bar+'\n\n')
    text.insert(INSERT, cb_get+'\n')

view_cb()

root.mainloop()
