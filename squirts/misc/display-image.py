"""Display image.
Stand-alone example code from Tk Assistant.

   pip3 install pillow
   ducks.jpg in current dir (supplied)

stevepython.wordpress.com
pyshambles.blogspot.com
"""
from tkinter import Label, LabelFrame, RIDGE, Tk
from PIL import Image, ImageTk

root = Tk()
root.title('Display image example')

# Create frame for the image.
img_frame = LabelFrame(root, relief=RIDGE)
img_frame.grid(padx=18, pady=18)

# Insert image, note:image file needs to be in same dir as this script
# runs from or you will need to give a file location of the image.
# Rename ducks.jpg to your image below. jpg, png, gif etc.
img = Image.open('ducks.jpg')
PHOTO = ImageTk.PhotoImage(img)

img_lab = Label(img_frame, image=PHOTO)
img_lab.img = PHOTO
img_lab.grid()

root.mainloop()
