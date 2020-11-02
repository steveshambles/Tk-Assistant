"""Date picker dialog.
   Stand-alone example from Tk Assistant.
   stevepython.wordpress.com
   pyshambles.blogspot.com

requirements:
pip3 install tkcalendar
"""
from tkinter import Button, Tk, Toplevel
from tkcalendar import Calendar

root = Tk()
root.withdraw() # Hide naff extra window.
root.title('Please choose a date')

def pick_date_dialog():
    """Display date picker dialog, print date selected when OK clicked."""
    def print_sel():
        """Print date selected."""
        selected_date = (cal.get_date())
        print(selected_date)

    top = Toplevel(root)
    # Defaults to today's date.
    cal = Calendar(top,
                   font='Arial 10', background='darkblue',
                   foreground='white', selectmode='day')

    cal.grid()
    Button(top, text='OK', command=print_sel).grid()

pick_date_dialog()

root.mainloop()
