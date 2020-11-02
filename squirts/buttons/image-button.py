"""Image button
   Stand-alone example from Tk Assistant.
   stevepython.wordpress.com
   pyshambles.blogspot.com
"""
from tkinter import Button, LabelFrame, PhotoImage, Tk

root = Tk()
root.title('Image Button example')

main_frame = LabelFrame(root)
main_frame.grid()

def bbc_btn():
    """Image Button was clicked."""
    print('Button clicked')

# The image is required in current dir that this script is run from.
# You can use gif, png, jpg etc.
bbc_img_btn = Button(main_frame, text='BBC News', command=bbc_btn)
PHOTO = PhotoImage(file='bbc-55x18.png')

# Use width and height to adjust size button.
bbc_img_btn.config(image=PHOTO, width='85', height='30')
bbc_img_btn.grid(padx=20, pady=20)

root.mainloop()
