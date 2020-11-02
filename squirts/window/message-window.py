"""Message Widow.
Stand-alone example from Tk Assistant.
stevepython.wordpress.com
pyshambles.blogspot.com
"""
from tkinter import Message, Tk

root = Tk()
root.title('Message window example')

msg_text = 'What you think of me is none of my business.'

msg = Message(root, text=msg_text)
msg.config(bg='springgreen', font=('verdant', 24, 'italic'))
msg.grid()

root.mainloop()
