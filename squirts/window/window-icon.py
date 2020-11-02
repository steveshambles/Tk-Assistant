"""Window icon.
Stand-alone example from Tk Assistant.
stevepython.wordpress.com
pyshambles.blogspot.com
"""
from tkinter import Tk

# Create window.
root = Tk()
root.title('Changed icon example')

# Ensure the .ico file is in same dir
# as this source code is run from.

# Rename disk.ico to your own icon
root.iconbitmap('disk.ico')

root.mainloop()
