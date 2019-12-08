"""
Tkinter Toolbar v2 by Tk Assistant.
upgrade of snippet 111.

pip3 install pillow
also requires ttips.py in current dir
and icons in a folder named icons.

Original code source:unknown.
Edited and enhanced significantly
by Steve Shambles. Dec 2019
stevepython.wordpress.com

free icons sourced from:
https://all-free-download.com/free-icon/download/
free_icons_for_developers_icons_pack_120612_download.html
"""

from tkinter import Button, Frame, INSERT, LEFT, RIGHT
from tkinter import Scrollbar, Text, Tk, TOP, X, Y

from PIL import Image, ImageTk

import ttips

root = Tk()
root.title('Tkinter Toolbar example')

def callback(icon_msg):
    """Print in textbox which icon has been clicked on"""
    text.insert(INSERT, icon_msg+'\n')

# Create the toolbar as a frame.
toolbar = Frame(root, borderwidth=2, bg='slategray4', relief='raised')

# Load all the images first as PNGs and use ImageTk to convert
# them to usable Tkinter images.
img1 = Image.open(r'icons/about.png')
useImg1 = ImageTk.PhotoImage(img1)
img2 = Image.open(r'icons/help.png')
useImg2 = ImageTk.PhotoImage(img2)
img3 = Image.open(r'icons/website.png')
useImg3 = ImageTk.PhotoImage(img3)
img4 = Image.open(r'icons/search.png')
useImg4 = ImageTk.PhotoImage(img4)
img5 = Image.open(r'icons/music.png')
useImg5 = ImageTk.PhotoImage(img5)
img6 = Image.open(r'icons/exit.png')
useImg6 = ImageTk.PhotoImage(img6)

# Set up all the buttons for use on the toolbars.
about_btn = Button(toolbar, image=useImg1,
                   command=lambda: callback("clicked about icon"))
about_btn.pack(side=LEFT, fill=X)
ttips.Create(about_btn, 'About')

help_btn = Button(toolbar, image=useImg2,
                  command=lambda: callback("clicked help icon"))
help_btn.pack(side=LEFT, fill=X)
ttips.Create(help_btn, 'Help')

website_btn = Button(toolbar, image=useImg3,
                     command=lambda: callback("clicked visit blog icon"))
website_btn.pack(side=LEFT, fill=X)
ttips.Create(website_btn, 'Visit blog')

search_btn = Button(toolbar, image=useImg4,
                    command=lambda: callback("clicked search icon"))
search_btn.pack(side=LEFT, fill=X)
ttips.Create(search_btn, 'Search')

music_btn = Button(toolbar, image=useImg5,
                   command=lambda: callback("clicked music icon"))
music_btn.pack(side=LEFT, fill=X)
ttips.Create(music_btn, 'Play Music')

exit_btn = Button(toolbar, image=useImg6,
                  command=root.destroy)
exit_btn.pack(side=LEFT, fill=X)
ttips.Create(exit_btn, 'Exit')

# Add the toolbar.
toolbar.pack(side=TOP, fill=X)

# Set up a Text box and scroll bar.
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

text = Text(root)
text.pack()

text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text.yview)

root.mainloop()
