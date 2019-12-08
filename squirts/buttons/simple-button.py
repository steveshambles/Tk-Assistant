"""Simple button.
   Stand-alone example from Tk Assistant.
   stevepython.wordpress.com"""

from tkinter import Button, LabelFrame, Tk

root = Tk()
root.title('Simple button')

def clkd_btn():
    """Button was clicked."""
    print('clicked')

main_frame = LabelFrame(root, text='Button')
main_frame.grid(padx=20, pady=20)

btn_one = Button(main_frame, bg='skyblue', text='Click Me',
                 command=clkd_btn)
btn_one.grid(pady=15, padx=15)

root.mainloop()
