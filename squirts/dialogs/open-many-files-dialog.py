"""Open many files dialog.
   Stand-alone example from Tk Assistant.
   stevepython.wordpress.com
   pyshambles.blogspot.com
"""
from tkinter import filedialog, Tk

root = Tk()
root.withdraw()

files_slctd = filedialog.askopenfilenames(title='Select files while holding down shift')

print('The files you selected are:\n')

for files in files_slctd:
    print(files)

root.mainloop()
