"""Display image.
   Stand-alone example code from Tk Assistant.
   stevepython.wordpress.com

   pip3 install pillow
"""

from tkinter import Label, LabelFrame, RIDGE, Tk

from PIL import Image, ImageTk

root = Tk()
root.title('Display image example')

# Create frame for the image
main_frame = LabelFrame(root, relief=RIDGE)
main_frame.grid(padx=18, pady=18)

# Insert image, note:image file needs to be in same dir as this script
# runs from or you will need to give a file location of the image.
# Rename ducks.jpg to your image below. jpg, png, gif etc.
img = Image.open('ducks.jpg')
PHOTO = ImageTk.PhotoImage(img)
la_bel = Label(main_frame, image=PHOTO)
la_bel.img = PHOTO
la_bel.grid()

root.mainloop()
