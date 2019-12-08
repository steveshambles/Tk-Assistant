"""Color picker dialog.
   Stand-alone example from Tk Assistant.
   stevepython.wordpress.com"""

from tkinter import Tk
from tkinter.colorchooser import askcolor

root = Tk()
root.withdraw()

# Hex value of color returned in tuple askcolor.
get_colour = askcolor()
print('Colour picked: ', get_colour[1])

root.mainloop()
