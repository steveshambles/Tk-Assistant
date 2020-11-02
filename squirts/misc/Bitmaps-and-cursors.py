"""Tkinters internal bitmaps and cursors
TkAssistant stand-alone example.
stevepython.wordpress.com
pyshambles.blogspot.com
"""
from tkinter import   Button, LabelFrame, Tk

root = Tk()
root.title('Bitmaps and cursors')
root.geometry('250x150')

def clkd_btn(txt):
    """A button was clicked. Report which in console."""
    print('Clicked on ' + txt)

main_frame = LabelFrame(root, fg='blue',
                        text='Tk internal bitmaps and cursors\n'
                        'Move mouse over a button')
main_frame.grid(padx=30, pady=10)


info_btn = Button(main_frame, bg='plum', bitmap='info',
                  cursor='exchange', command=lambda: clkd_btn('Info btn'))
info_btn.grid(pady=5, padx=5, row=0, column=0)

hglass_btn = Button(main_frame, bg='gold', bitmap='hourglass',
                    cursor='pirate', command=lambda: clkd_btn('Hour-glass btn'))
hglass_btn.grid(pady=5, padx=5, row=0, column=1)

quest_btn = Button(main_frame, bg='lightgreen', bitmap='question',
                   cursor='crosshair', command=lambda: clkd_btn('Question mark btn'))
quest_btn.grid(pady=5, padx=5, row=0, column=2)

err_btn = Button(main_frame, bg='skyblue', bitmap='error',
                 cursor='heart', command=lambda: clkd_btn('Error btn'))
err_btn.grid(pady=5, padx=5, row=0, column=3)

warn_btn = Button(main_frame, bg='orange', bitmap='warning',
                  cursor='hand1', command=lambda: clkd_btn('Warning btn'))
warn_btn.grid(pady=5, padx=5, row=0, column=4)

qhead_btn = Button(main_frame, bg='bisque', bitmap='questhead',
                   cursor='watch', command=lambda: clkd_btn('Question head btn'))
qhead_btn.grid(pady=5, padx=5, row=1, column=0)

grey75_btn = Button(main_frame, bitmap='gray75',
                    cursor='sailboat', command=lambda: clkd_btn('Grey 75 btn'))
grey75_btn.grid(pady=5, padx=5, row=1, column=1)

grey50_btn = Button(main_frame, bitmap='gray50',
                    cursor='shuttle', command=lambda: clkd_btn('Grey 50 btn'))
grey50_btn.grid(pady=5, padx=5, row=1, column=2)

grey25_btn = Button(main_frame, bitmap='gray25',
                    cursor='spraycan', command=lambda: clkd_btn('Grey 25 btn'))
grey25_btn.grid(pady=5, padx=5, row=1, column=3)

grey12_btn = Button(main_frame, bitmap='gray12',
                    cursor='watch', command=lambda: clkd_btn('Grey 12 btn'))
grey12_btn.grid(pady=5, padx=5, row=1, column=4)

root.mainloop()
