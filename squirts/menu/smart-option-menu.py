"""Smart Option Menu
   Stand-alone example from Tk Assistant.
   stevepython.wordpress.com

requirement:
pip3 install tk_tools
"""
from tkinter import Label, Tk

import tk_tools

root = Tk()
root.title('Smart option menu example')
root.geometry('190x60')

def smart_om(value):
    """Print selection."""
    print('You selected option:', str(value))

value_label = Label(root, text='')
value_label.grid(row=1, column=1, sticky='ew')

Label(root, text='\nSelect your\nstar sign').grid(row=0,
                                                  column=0, sticky='ew')

drop_down = tk_tools.SmartOptionMenu(root, ['Aries', 'Aquarius', 'Cancer',
                                            'Capricorn', 'Gemini', 'leo',
                                            'Libra', 'Pisces', 'Sagittarius',
                                            'Scorpio', 'Taurus', 'Virgo'],
                                     callback=smart_om)

drop_down.grid(row=0, column=1, sticky='ew')

root.mainloop()
