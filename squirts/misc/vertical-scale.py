"""Vertical scale.
   Stand-alone code from Tk Assistant.
   stevepython.wordpress.com"""

from tkinter import Canvas, Scale, Tk, VERTICAL

root = Tk()
root.title('Vertical scale example')

def setHeight(canvas, heightStr):
    """Set scale height."""
    height = 21
    height = height + 21
    y2 = height - 30
    print(heightStr)# Holds current scale pointer.
    if y2 < 21:
        y2 = 21

canvas = Canvas(root, width=65, height=50, bd=0, highlightthickness=0)
scale = Scale(root,
              orient=VERTICAL,
              length=284,
              from_=0,
              to=250,
              bg='skyblue',
              tickinterval=25,
              command=lambda h, c=canvas: setHeight(c, h))

scale.grid(row=0, column=0, sticky='NE')

# Starting point on scale.
scale.set(125)

root.mainloop()
