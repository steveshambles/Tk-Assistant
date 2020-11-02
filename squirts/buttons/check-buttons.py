"""Checkbuttons.
   Stand-alone example from Tk Assistant.
   stevepython.wordpress.com
   pyshambles.blogspot.com
"""
from tkinter import Button, Checkbutton, E, IntVar, LabelFrame
from tkinter import messagebox, Tk, W

root = Tk()
root.title('Check Buttons examples')

def var_states():
    """Check and show which buttons user has selected."""
    if VAR1.get() == 1 and VAR2.get() == 1:
        msg_box_txt = 'Both buttons checked'

    if VAR1.get() == 1 and VAR2.get() == 0:
        msg_box_txt = 'Python V2 checked'

    if VAR1.get() == 0 and VAR2.get() == 1:
        msg_box_txt = 'Python V3 checked'

    if VAR1.get() == 0 and VAR2.get() == 0:
        msg_box_txt = 'Nothing checked'

    messagebox.showinfo('Checkbutton', msg_box_txt)

main_frame = LabelFrame(root, text='Please select what Python you use')
main_frame.grid(padx=10, pady=10)

VAR1 = IntVar()
Checkbutton(main_frame, text='Python V2', variable=VAR1).grid(row=0, sticky=W)

VAR2 = IntVar()
Checkbutton(main_frame, text='Python V3', variable=VAR2).grid(row=1, sticky=W)
Button(main_frame, text='Show', bg='plum',
       command=var_states).grid (row=3, column=1, sticky=E, pady=5)

root.mainloop()
