"""Save file dialog.
   Stand-alone example from Tk Assistant.
   stevepython.wordpress.com
   pyshambles.blogspot.com
"""
from tkinter import filedialog, Tk

root = Tk()
root.withdraw()

save_file = filedialog.asksaveasfilename(title='Save file')
print('The file name you saved is:\n' + save_file)

root.mainloop()
