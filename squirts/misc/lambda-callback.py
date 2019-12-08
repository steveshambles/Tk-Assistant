"""Lambda callback.
   Stand-alone code from Tk Assistant.
   stevepython.wordpress.com"""

from tkinter import Button, LabelFrame, Tk

root = Tk()
root.title('Lambda callback example')

def clkd_but(butn_num):
    """A button was clicked, print which one."""
    print(butn_num)

main_frame = LabelFrame(root, text='')
main_frame.grid()

btn_one = Button(main_frame, bg='skyblue', text='Click Me 1',
                 command=lambda: clkd_but("clicked button 1"))
btn_one.grid()

btn_two = Button(main_frame, bg='orange', text='Click Me 2',
                 command=lambda: clkd_but("clicked button 2"))
btn_two.grid()

root.mainloop()
