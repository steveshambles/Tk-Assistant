"""Message Widow.
   Stand-alone example from Tk Assistant.
   stevepython.wordpress.com"""

from tkinter import Message, Tk

root = Tk()
root.title('Message window example')

msg_text = 'Whoever invented auto-correct '  \
            'should burn in hello.'

msg = Message(root, text=msg_text)
msg.config(bg='springgreen', font=('verdant', 24, 'italic'))
msg.grid()

root.mainloop()
