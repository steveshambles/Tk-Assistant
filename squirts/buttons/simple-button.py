"""Simple button.
   Stand-alone example from Tk Assistant.
   stevepython.wordpress.com
   pyshambles.blogspot.com
"""
from tkinter import Button, LabelFrame, Tk

root = Tk()
root.title('Button')

def clkd_btn():
    """Button was clicked."""
    print('Button was clicked')

main_frame = LabelFrame(root, text='Simple button example')
main_frame.grid(padx=10, pady=10)

btn_one = Button(main_frame, bg='indianred', text='Click Me',
                 command=clkd_btn)
btn_one.grid(pady=5, padx=5)

root.mainloop()
