"""
Colour Sliders code from Tk Assistant.
from the book Adventures In Python
Edited and updated by Steve Shambles
Dec 2019.
stevepython.wordpress.com
pyshambles.blogspot.com
"""
from tkinter import Canvas, END, Entry, Scale, Tk

root = Tk()
root.title('Colour Sliders example')

def slider_update(source):
    """Update sliders values."""
    red = red_slider.get()
    green = green_slider.get()
    blue = blue_slider.get()

    colour = '#%02x%02x%02x' % (red, green, blue)
    Canvas.config(bg=colour)
    hex_text.delete(0, END)
    hex_text.insert(0, colour)

red_slider = Scale(root, from_=0, to=255, command=slider_update)
green_slider = Scale(root, from_=0, to=255, command=slider_update)
blue_slider = Scale(root, from_=0, to=255, command=slider_update)

Canvas = Canvas(root, width=200, height=200)

hex_text = Entry(root)

red_slider.grid(row=1, column=1)
green_slider.grid(row=1, column=2)
blue_slider.grid(row=1, column=3)
Canvas.grid(row=2, column=1, columnspan=3)
hex_text.grid(row=3, column=1, columnspan=3)

root.mainloop()
