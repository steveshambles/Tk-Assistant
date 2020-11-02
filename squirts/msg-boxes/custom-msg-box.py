"""Custom message box.
   Stand-alone example from Tk Assistant.
   stevepython.wordpress.com
   pyshambles.blogspot.com
"""
from tkinter import Button, Label, Tk, Toplevel

root = Tk()
root.title('Your main program window')

custom_mbox = Toplevel(root)
custom_mbox.resizable(False, False)
#custom_mbox.wm_overrideredirect(True) # Use this line for no window bar.
custom_mbox.title('Custom msgbox')
custom_mbox.attributes('-topmost', 1) # Bring custom window to front.

def btn_clk():
    """Button was clicked in custom messagebox."""
    print('Clicked button')
    custom_mbox.destroy()

cstm_mb_label = Label(custom_mbox,
                      text='This is an example of a custom pop up box.\n'
                      'You can add almost any feature you can think of\n'
                      'inside this window.\n\nThe main benefit of using your\n'
                      'own pop up is that it is non-code-blocking, unlike\n'
                      'the built in pop up boxes which stop the code\n '
                      'execution until a button is clicked.')
cstm_mb_label.grid()

btn = Button(custom_mbox, bg="skyblue", fg="black", text='  OK  ',
             command=btn_clk)
btn.grid()

root.mainloop()
