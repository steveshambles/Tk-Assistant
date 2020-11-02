"""Relief types.
   Stand-alone example from Tk Assistant.
   stevepython.wordpress.com
   pyshambles.blogspot.com
"""
from tkinter import Button, E, FLAT, GROOVE, RAISED, RIDGE, SUNKEN, Tk, W

root = Tk()
root.title('Relief types')

flat_btn = Button(root, text="FLAT", font='helvetica', bg='orange',
                  width=25, border=4, relief=FLAT)
flat_btn.grid(pady=10, padx=15, sticky=W+E)

groove_btn = Button(root, text="GROOVE", bg='yellow', font='helvetica',
                    border=4, relief=GROOVE)
groove_btn.grid(pady=10, padx=15, sticky=W+E)

raised_btn = Button(root, text="RAISED", font='helvetica', bg='powderblue',
                    border=4, relief=RAISED)
raised_btn.grid(pady=10, padx=15, sticky=W+E)

ridge_btn = Button(root, text="RIDGE", bg='springgreen', font='helvetica',
                   border=4, relief=RIDGE)
ridge_btn.grid(pady=10, padx=15, sticky=W+E)

sunken_btn = Button(root, text="SUNKEN", font='helvetica', bg='indianred',
                    border=4, relief=SUNKEN)
sunken_btn.grid(pady=10, padx=15, sticky=W+E)

root.mainloop()
