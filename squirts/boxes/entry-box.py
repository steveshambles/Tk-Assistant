"""Entry box.
   Stand-alone example from Tk Assistant.
   stevepython.wordpress.com
   https://pyshambles.blogspot.com/
   """
from tkinter import E, Entry, LabelFrame, messagebox, Tk, W

root = Tk()
root.title('Entry box')

def ebox_display():
    """Display contents of entry box."""
    txt = entry_box.get()
    messagebox.showinfo('Information',
                        'Entry box contains the text:\n'+str(txt))

main_frame = LabelFrame(root)
main_frame.grid(padx=5, pady=8)

entry_box = Entry(main_frame, bd=3, bg='gold')
entry_box.grid(sticky=W+E, padx=5, pady=5)
entry_box.insert(0, 'Type text, press return')
entry_box.focus()

root.bind("<Return>", lambda x: ebox_display())

root.mainloop()
