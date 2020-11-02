"""Radio buttons.
   Stand-alone example from Tk Assistant.
   stevepython.wordpress.com
   pyshambles.blogspot.com
"""
from tkinter import IntVar, LabelFrame, messagebox, Radiobutton, Tk, W

root = Tk()
root.title('Radio Buttons')

def radio_sel():
    """Display radio button selected by user."""
    radio = VRB.get()
    messagebox.showinfo('You picked:', 'Radio button '+str(radio))

main_frame = LabelFrame(root, text='Select a Radio button')
main_frame.grid(padx=10, pady=13)

VRB = IntVar()
Radiobutton(main_frame, text='One', command=radio_sel, variable=VRB,
            value=1).grid(stick=W)
Radiobutton(main_frame, text='Two', command=radio_sel, variable=VRB,
            value=2).grid(sticky=W)
Radiobutton(main_frame, text='Three', command=radio_sel, variable=VRB,
            value=3).grid(sticky=W)
Radiobutton(main_frame, text='Four', command=radio_sel, variable=VRB,
            value=4).grid(sticky=W)

root.mainloop()
