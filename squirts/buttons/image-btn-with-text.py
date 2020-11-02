"""Image button with text
   Stand-alone example from Tk Assistant.
   stevepython.wordpress.com
   pyshambles.blogspot.com
"""
from tkinter import Button, Frame, PhotoImage, Tk, TOP

root = Tk()
root.title('Image Button with text example')

main_frame = Frame(root)
main_frame.grid()

def yt_btn():
    """Image Button was clicked."""
    print('Button clicked')

# Note the "compound=TOP" for img to text placement.
PHOTO = PhotoImage(file=r'ytube.png')
yt_img_btn = Button(main_frame, text='YouTube', compound=TOP,
                    command=yt_btn)

# Use width and height to adjust size button.
yt_img_btn.config(image=PHOTO, width='80', height='45')
yt_img_btn.grid(padx=20, pady=20)

root.mainloop()
