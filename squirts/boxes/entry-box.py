"""Entry box.
   Stand-alone example from Tk Assistant.
   stevepython.wordpress.com"""

from tkinter import E, Entry, LabelFrame, messagebox, Tk, W

root = Tk()
root.title('Entry box')

def rc_ebox(event):
    """Display contents of entry box."""
    del event
    txt = entry_box.get()
    messagebox.showinfo('Information',
                        'Entry box contains the text: '+str(txt))

main_frame = LabelFrame(root)
main_frame.grid(padx=5, pady=8)

entry_box = Entry(main_frame, bd=3, bg='gold')
entry_box.grid(sticky=W+E, padx=5, pady=5)
entry_box.insert(0, 'Type text and then right click mouse')
entry_box.focus()

entry_box.bind('<Button-3>', rc_ebox)

root.mainloop()
