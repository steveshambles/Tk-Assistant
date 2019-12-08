"""Centre window.
   Stand-alone example from Tk Assistant.
   stevepython.wordpress.com
   source:https://bbs.archlinux.org/viewtopic.php?id=149559
   Note: may not work properly on Linux.
   """

from tkinter import Tk
from tkinter.ttk import Label

root = Tk()
root.title('Centre window on screen')
Label(root, text='This window should be in the centre of your screen.').grid()

root.withdraw()
root.update_idletasks()  # Update 'requested size' from geometry manager.

scrn_wdth = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
scrn_hght = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.geometry("+%d+%d" % (scrn_wdth, scrn_hght))

# This seems to draw the window frame immediately, so only call deiconify()
# after setting correct window position.
root.deiconify()

root.mainloop()
