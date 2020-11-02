"""Simple scale.
Stand-alone example from Tk Assistant.

By Steve Shammbles.
stevepython.wordpress.com
pyshambles.blogspot.com
"""
from tkinter import Button, HORIZONTAL, Scale, Tk

root = Tk()
root.title('Simple scale example')

def final_setting():
    """Display scale value setting if OK button clicked."""
    scale_setting = scale_meter.get()
    print('Scale reads:', scale_setting)

scale_meter = Scale(root, fg='green',
                    from_=0, to=100, orient=HORIZONTAL)
scale_meter.grid(padx=40, pady=10)

ok_btn = Button(root, bg='gold', text='OK', command=final_setting)
ok_btn.grid(pady=10)

root.mainloop()
