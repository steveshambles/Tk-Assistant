"""Open askdirectory dialog.
   Stand-alone example from Tk Assistant.
   stevepython.wordpress.com
   pyshambles.blogspot.com
"""
from tkinter import filedialog, Tk

root = Tk()
root.withdraw()

# Open the file requestor.
folder_slctd = filedialog.askdirectory()
print('The folder you selected is:\n' + folder_slctd)

root.mainloop()
