"""Listbox.
   Stand-alone example from Tk Assistant.
   stevepython.wordpress.com
   https://pyshambles.blogspot.com/
   """
from tkinter import BOTTOM, LabelFrame, Listbox, messagebox
from tkinter import RIGHT, Scrollbar, Tk, X, Y

root = Tk()
root.title('Listbox by TK Assistant')
root.resizable(False, False)

def double_clicked(event):
    """Double clicked mouse on listbox item. Report which item."""
    ev_w = event.widget
    idx = int(ev_w.curselection()[0])
    value = ev_w.get(idx)
    messagebox.showinfo('About', 'Listbox double clicked on:\n'+str(value))

def right_clicked(event):
    """Right clicked mouse on item."""
    ev_w = event.widget
    idx = int(ev_w.curselection()[0])
    value = ev_w.get(idx)
    messagebox.showinfo('About', 'Listbox right clicked on:\n'+str(value))

def mid_clicked(event):
    """Middle clicked mouse on item."""
    ev_w = event.widget
    idx = int(ev_w.curselection()[0])
    value = ev_w.get(idx)
    messagebox.showinfo('About', 'Listbox middle clicked on:\n'+str(value))

main_frame = LabelFrame(root)
main_frame.grid(padx=8, pady=8)

lst_bx = Listbox(
    master=main_frame,
    selectmode='single',
    width=36,
    height=5,
    fg='black',
    bg='springgreen')

scrbar_vert = Scrollbar(main_frame, orient='vertical')
scrbar_vert.pack(side=RIGHT, fill=Y)
lst_bx.configure(yscrollcommand=scrbar_vert.set)
scrbar_vert.configure(command=lst_bx.yview)

scrbar_horiz = Scrollbar(main_frame, orient='horizontal')
scrbar_horiz.pack(side=BOTTOM, fill=X)
lst_bx.configure(xscrollcommand=scrbar_horiz.set)
scrbar_horiz.configure(command=lst_bx.xview)

lst_bx.pack()
lst_bx.bind('<Double-1>', double_clicked)
lst_bx.bind('<Button-3>', right_clicked)
lst_bx.bind('<Button-2>', mid_clicked)

lst_bx.insert('end', 'It hurt because it mattered. – John Green')
lst_bx.insert('end', 'Be so good they can’t ignore you. – Steve Martin')
lst_bx.insert('end', 'Everything you can imagine is real. – Pablo Picasso')
lst_bx.insert('end', 'No one can make you feel inferior without your consent.'
              '― Eleanor Roosevelt')

lst_bx.insert('end', 'You only live once, but if you do it right,'
                     'once is enough. ― Mae West')

lst_bx.insert('end', 'Always forgive your enemies; nothing annoys them so'
              'much. ― Oscar Wilde')

lst_bx.insert('end', 'If you always tell the truth, you dont have to'
                     'remember anything. ― Mark Twain')

messagebox.showinfo('Listbox demo', 'Double click, right click\nor middle click a selection.')

root.mainloop()
