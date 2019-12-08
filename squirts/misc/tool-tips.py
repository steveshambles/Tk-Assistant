"""
Tooltips.
Stand-alone code from Tk Assistant..
stevepython.wordpress.com

requires:
ttips.py in same directory this script is run from.
"""
from tkinter import Button, Label, Tk

import ttips

root = Tk()
root.title('Tooltips examples')

#create some example buttons
btn1 = Button(root, text='Button 1')
btn1.grid(sticky='WE')
btn2 = Button(root, text='Button 2')
btn2.grid(sticky='WE')
btn3 = Button(root, text='Button 3')
btn3.grid(sticky='WE')
btn4 = Button(root, text='Button 4')
btn4.grid(sticky='WE')
btn5 = Button(root, text='Button 5. 8 sec timer')
btn5.grid(sticky='WE')
btn6 = Button(root, text='Button 6. All together now!')
btn6.grid(sticky='WE')

# To show how to use on other widgets, create a label.
txt_lab = Label(root, bg='plum', text='This is text on a simple label')
txt_lab.grid()


# Add the tooltips text to the buttons.
#--------------------------------------
# tooltips.Create(widget, text, bgcol, fgcol, fontname, fontsize, showtime)

# Optional background\foreground color, or defaults to yellow-black.

# Optional fontname, default times, fontsize, default 8,

# showtime, default is 2 (seconds)

# Use '\n' in text for multi-lines.

ttips.Create(btn1, 'Default tooltip over button 1')

ttips.Create(btn2, 'Tooltip with colors over button 2',
             bgcol='green', fgcol='white')

ttips.Create(btn3, 'Font changed to helvetica over btn 3',
             fontname='helvetica')

ttips.Create(btn4, 'Tooltip fontsize changed to 16, over button 4',
             fontsize=16)

ttips.Create(btn5, 'This will display for 8 seconds,\n'
                   'unless you move the mouse off the button\n'
                   'before that time is up.', showtime=8)

ttips.Create(btn6, 'All options used. This will display for 12 seconds.\n'
                   'Using comic sans font 24.\n'
                   'Orange background, black text.', bgcol='orange',  \
                   fontname='Comic Sans MS', fontsize=24, showtime=12)

# And on other widgets, like a label for example
ttips.Create(txt_lab, 'Default tooltip over a label')

root.mainloop()
