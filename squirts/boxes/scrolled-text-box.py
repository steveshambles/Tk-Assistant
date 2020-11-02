"""Scrolled text box.
   Stand-alone example from Tk Assistant.
   stevepython.wordpress.com
   https://pyshambles.blogspot.com/
   """
from tkinter import Button, END, INSERT, LabelFrame, S, scrolledtext, Tk

root = Tk()
root.title('Tk Assistant Scolled Text Box example')
root.resizable(False,False)

def clear_txt():
    """Clear text from box."""
    scr_txt_box.delete(1.0, END)

main_frame = LabelFrame(root, fg='blue', text='Scrolled text box')
main_frame.grid(padx=10, pady=10)

scr_txt_box = scrolledtext.ScrolledText(main_frame, bg='gold',
                                        width=40, height=10)
scr_txt_box.grid(row=3, column=0)

scr_txt_box.insert(INSERT, 'This is a scrolled textbox.\n\nTry typing.')

Button(main_frame, bg='plum', text='Clear the text',
       command=clear_txt).grid(row=0, column=0, sticky=S, pady=8)

root.mainloop()
