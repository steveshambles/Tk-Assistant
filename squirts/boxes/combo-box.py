"""Combobox.
   Stand-alone example from Tk Assistant.
   stevepython.wordpress.com
   https://pyshambles.blogspot.com/
   """
from tkinter import Button, E, LabelFrame, messagebox, Tk, W
from tkinter.ttk import Combobox

root = Tk()
root.title('Combobox example')

def clkd_btn():
    """Display selection."""
    sel_item = combo_one.get()

    if sel_item == 'Select an item':
        return

    messagebox.showinfo('User choice', 'You Selected:\n\n'+str(sel_item))

main_frame = LabelFrame(root)
main_frame.grid(padx=8, pady=8)

combo_one = Combobox(main_frame)
combo_one['values'] = ('Select an item', 'Art', 'Cats', 'Celeb', 'Dogs')
combo_one.current(0)
combo_one.grid(padx=5, pady=5)

btn_one = Button(main_frame, bg='salmon', text='Click Me', command=clkd_btn)
btn_one.grid(sticky=W+E, padx=5, pady=5)

root.mainloop()
