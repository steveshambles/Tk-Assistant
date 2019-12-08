"""Right click context menu.
   Stand-alone example from Tk Assistant.
   stevepython.wordpress.com"""

from tkinter import Frame, Menu, Tk

root = Tk()
root.title('Right Click Menu example')

main_frame = Frame(root, width=250, height=250, bg='green')
main_frame.grid()

def paste():
    """Called when Paste selected from right click menu."""
    print('Paste selected')

def copy():
    """Called when Copy selected from right click menu."""
    print('Copy selected')

def popup(event):
    """On right click display popup menu at mouse position."""
    rc_menu.post(event.x_root, event.y_root)

# Bind mouse right click to frame.
main_frame.bind('<Button-3>', popup)

# Create the popup menu.
rc_menu = Menu(root, tearoff=0)
rc_menu.add_command(label='Copy', command=copy)
rc_menu.add_command(label='Paste', command=paste)
rc_menu.add_command(label='Quit', command=root.destroy)

root.mainloop()
