"""
TK Assistant V2.0w Dec 8th 2019

By Steve Shambles
https://stevepython.wordpress.com/

pip3 install pyperclip

needed to run examples:
--------------------------
Smart option menu: pip3 install tk_tools
display image: pip3 install pillow
tooltips: ttips.py in same directory script is run from.
date picker: pip3 install tkcalendar
toolbar with icons, needs icons folder and ttips.py
-----
v2.0w checked all squirts, improved, linted them.
V1.9w added quick start messagebox text
      finished adding items to drop-down menu
      removed, remmed out, status bar-can't find a use for it at mo.
V1.8w added quick start icon
      rearranged order of icons
      centered icons
V1.7w added read tk docs icon and menu item.
      started rechecking each squirt.
      added ytube icon and link
      added reddit icon and link
      added py forum gui icon and link
v1.6w added open squirts folder and contact me menu icons.
      Code tidy.
      more file and folder checks.
V1.5w added Simple scale squirt.
V1.4w added colour sliders squirt.
V1.3w Added date and clock using threading timer in main gui and as a squirt.

V1.2w added working icon toolbar to actual Tk Assistant GUI.
      ask yn to exit.
      justified icons left, bigger tooltips
      added status bar
      added TkAss icon

v1.1w added toolbar with icons squirt
"""

import os
import sys
from threading import Timer
import time
from tkinter import Button, E, Frame, Label, LabelFrame
from tkinter import Menu, messagebox, RIDGE, Tk, W
from tkinter.ttk import Combobox
import webbrowser

from PIL import Image, ImageTk
import pyperclip

root = Tk()
root.title('TK Assistant V2.0w - By Steve Shambles. 45 squirts.')
root.resizable(False, False)


def check_files():
    """Check if files exists, if not warn, exit."""

    tka = ('squirts')
    check_dir = os.path.isdir(tka)
    if not check_dir:
        messagebox.showwarning('Folder missing:', 'The squirts folder is '
                               'missing.\nCannot continue.\n Please re-install.')
        root.destroy()
        sys.exit()

    tka = ('icons')
    check_dir = os.path.isdir(tka)
    if not check_dir:
        messagebox.showwarning('Folder missing:', 'The icons folder is '
                               'missing.\nCannot continue.\n Please re-install.')
        root.destroy()
        sys.exit()

    tka = ('bbc-55x18.png')
    check_file = os.path.isfile(tka)

    if not check_file:
        messagebox.showwarning('File missing:', 'bbc-55x18.png is missing '
                               'Cannot continue.\n Please re-install.')
        root.destroy()
        sys.exit()

    tka = ('disk.ico')
    check_file = os.path.isfile(tka)
    if not check_file:
        messagebox.showwarning('File missing:', 'disk.ico is missing '
                               'Cannot continue.\n Please re-install.')

        root.destroy()
        sys.exit()

    tka = ('ducks.jpg')
    check_file = os.path.isfile(tka)
    if not check_file:
        messagebox.showwarning('File missing:', 'ducks.jpg is missing '
                               'Cannot continue.\n Please re-install.')
        root.destroy()
        sys.exit()

    tka = ('first_aid.ico')
    check_file = os.path.isfile(tka)
    if not check_file:
        messagebox.showwarning('File missing:', 'first_aid.ico is missing '
                               'Cannot continue.\n Please re-install.')
        root.destroy()
        sys.exit()

    tka = ('ttips.py')
    check_file = os.path.isfile(tka)
    if not check_file:
        messagebox.showwarning('File missing:', 'ttips.py is missing '
                               'Cannot continue.\n Please re-install.')
        root.destroy()
        sys.exit()

check_files()

# Need to do these two things after the file checks, not before.
root.iconbitmap('first_aid.ico')
import ttips


def help_page():
    """Visit online help page from file menu."""
    webbrowser.open('https://stevepython.wordpress.com/tk-assistant-help-page/')


def tk_docs():
    """Visit Python Tkinter documentation webpage."""
    webbrowser.open('https://docs.python.org/3.6/library/tk.html')


def visit_blog():
    """Visit my blog from file menu."""
    webbrowser.open('https://stevepython.wordpress.com/')

def about_menu():
    """Disply about message box from file menu."""
    messagebox.showinfo('About Tk Assistant',
                        'TK Assistant V2.0w\nIncludes 45 squirts.\n'
                        '\nFreeware.\nBy Steve Shambles,\nDec 2019.\n')

def exit_app():
    """Yes-no requestor to exit program."""
    ask_yn = messagebox.askyesno('Question',
                                 'Are you sure you want to exit Tk Assistant?')
    if ask_yn is False:
        return
    root.destroy()

def open_folder():
    """Open squirts folder in default file viewer."""
    cwd = os.getcwd()
    webbrowser.open(cwd+'/squirts')

def contact_me():
    """Use my blog contact page."""
    webbrowser.open('https://stevepython.wordpress.com/contact')

def ytube_tuts():
    """Go to Youtube and list tkinter tutorial videos."""
    webbrowser.open('https://www.youtube.com/results?search_query=python+tkinter+tutorial&sp=EgIIBQ%253D%253D')

def go_reddit():
    """Go to Reddit learn python forum for help."""
    webbrowser.open('https://www.reddit.com/r/learnpython/')

def python_forum():
    """Visit Python GUI forum for help."""
    webbrowser.open('https://python-forum.io/Forum-GUI')

def quick_help():
    """Quick start help pop up."""
    messagebox.showinfo('Tk Assistant V2.0w Quick Start',
                        'Choose an item from one of the drop-down combo boxes.\n'
                        'When you click the GET button on the right of your selection '
                        'the code will be copied to the clipboard.\n\n'
                        'You can now paste that code into your Python editor and\n'
                        'edit or run the code.\n\n'
                        'You will also be given the option to execute the code\n'
                        'from within Tk Assistant so that you can see a quick\n'
                        'demo what that widget does and how it works.\n\n'
                        'The toolbar at the top of the GUI has icons that are\n'
                        'mostly self explanatory, but If you move the mouse\n'
                        'pointer over an icon it will explain what it does\n'
                        'via a tooltip message.\n\n'
                        'As an example, click on the blue folder icon,\n'
                        '"View squirts folder".\n'
                        'This will take you via a file viewer to where the\n'
                        '"Squirts" used in Tk Assistant are stored.\n'
                        'Here you can use the squirts like any other .py file if you want.\n\n'
                        'You can also send me a message, or visit my Python blog,\n'
                        'which is chock full of hundreds of bits of useful source\n'
                        'code and articles for beginners.\n\n'
                        'Let me know if you found Tk Assistant useful, or if you have\n'
                        'constructive criticisms or ideas.\n\n'
                        'Enjoy. Steve Shambles. December 2019')

# Create the icon toolbar.
toolbar = Frame(root, borderwidth=2, bg='slategray4', relief='raised')
toolbar.grid(row=0, column=1, padx=20)

# Load all the images first as PNGs and use ImageTk to convert
# them to usable Tkinter images for icon menu.
img1 = Image.open(r'icons/about.png')
useImg1 = ImageTk.PhotoImage(img1)
img2 = Image.open(r'icons/help.png')
useImg2 = ImageTk.PhotoImage(img2)
img3 = Image.open(r'icons/website.png')
useImg3 = ImageTk.PhotoImage(img3)
img4 = Image.open(r'icons/folder.png')
useImg4 = ImageTk.PhotoImage(img4)
img5 = Image.open(r'icons/contact.png')
useImg5 = ImageTk.PhotoImage(img5)
img6 = Image.open(r'icons/readdoc.png')
useImg6 = ImageTk.PhotoImage(img6)
img7 = Image.open(r'icons/ytube.png')
useImg7 = ImageTk.PhotoImage(img7)
img8 = Image.open(r'icons/reddit.png')
useImg8 = ImageTk.PhotoImage(img8)
img9 = Image.open(r'icons/python.png')
useImg9 = ImageTk.PhotoImage(img9)
img10 = Image.open(r'icons/qstart32.png')
useImg10 = ImageTk.PhotoImage(img10)
img11 = Image.open(r'icons/exit.png')
useImg11 = ImageTk.PhotoImage(img11)

# Set up the buttons for use on the icon toolbar.
qstart_btn = Button(toolbar, image=useImg10,
                    command=quick_help)
qstart_btn.grid(row=0, column=0)
ttips.Create(qstart_btn, 'Quick start help',
             fontname='helvetica', fontsize=12)

about_btn = Button(toolbar, image=useImg1,
                   command=about_menu)
about_btn.grid(row=0, column=2)
ttips.Create(about_btn, 'About Tk Assistant',
             fontname='helvetica', fontsize=12)

help_btn = Button(toolbar, image=useImg2,
                  command=help_page)
help_btn.grid(row=0, column=1)
ttips.Create(help_btn, 'Online help page',
             fontname='helvetica', fontsize=12)

website_btn = Button(toolbar, image=useImg3,
                     command=visit_blog)
website_btn.grid(row=0, column=3)
ttips.Create(website_btn, 'Visit my Python blog',
             fontname='helvetica', fontsize=12)


folder_btn = Button(toolbar, image=useImg4,
                    command=open_folder)
folder_btn.grid(row=0, column=5)
ttips.Create(folder_btn, 'View squirts folder',
             fontname='helvetica', fontsize=12)


contact_btn = Button(toolbar, image=useImg5,
                     command=contact_me)
contact_btn.grid(row=0, column=4)
ttips.Create(contact_btn, 'Contact me',
             fontname='helvetica', fontsize=12)

tkdocs_btn = Button(toolbar, image=useImg6,
                    command=tk_docs)
tkdocs_btn.grid(row=0, column=6)
ttips.Create(tkdocs_btn, 'Read Tkinter documentation',
             fontname='helvetica', fontsize=12)

ytube_btn = Button(toolbar, image=useImg7,
                   command=ytube_tuts)
ytube_btn.grid(row=0, column=7)
ttips.Create(ytube_btn, 'Tkinter YouTube Video Tutorials',
             fontname='helvetica', fontsize=12)

reddit_btn = Button(toolbar, image=useImg8,
                    command=go_reddit)
reddit_btn.grid(row=0, column=8)
ttips.Create(reddit_btn, 'Get Tkinter help on Reddit',
             fontname='helvetica', fontsize=12)

py_forum_btn = Button(toolbar, image=useImg9,
                      command=python_forum)
py_forum_btn.grid(row=0, column=9)
ttips.Create(py_forum_btn, 'Visit Python GUI forum',
             fontname='helvetica', fontsize=12)

exit_btn = Button(toolbar, image=useImg11,
                  command=exit_app)
exit_btn.grid(row=0, column=10)
ttips.Create(exit_btn, 'Exit Tk Assistant',
             fontname='helvetica', fontsize=12)

# Add the toolbar.
toolbar.grid()

# Create frame for the digital date and clock.
date_clock = Label(root, bg='skyblue')
date_clock.grid(row=2, column=1, padx=20, pady=15, sticky=W+E)

def date_time():
    """Threading timer prints date and time every second."""
    curr_time = (time.strftime('%a, %d %b %Y. %H:%M:%S', time.gmtime()))
    date_clock.config(text=curr_time) #print updated clock.
    t = Timer(1.0, date_time)
    t.start()

# Starts the timer.
date_time()

# Add a status bar
# Removed for now as cant find a use for it yet.

##st_bar = Label(root, fg='green', text='Status: Ready',
##               bd=1, relief=SUNKEN, anchor=W)
##st_bar.grid(row=3, column=1, padx=20, pady=10, sticky=W+E)


# Handle executing squirts.
def ask_execute(py_file):
    """Pop up asks if user wants to execute code example."""

    # Check tk_tools installed on system before running
    # smart optio menu example.
    if py_file == ('squirts\menu\smart-option-menu.py'):
        try:
            import tk_tools
        except ImportError:
            messagebox.showwarning('Cannot run example:',
                                   'You need to pip install tk_tools\n'
                                   'for this example to work.')
            return

    # Check pillow installed
    if py_file == ('squirts\misc\display-image.py') or  \
                    py_file == ('squirts\menu\toolbar.py'):
        try:
            import PIL
        except ImportError:
            messagebox.showwarning('Cannot run example:',
                                   'You need to pip install pillow\n'
                                   'for this example to work.')
            return

    # Check tkcalendar installed
    if py_file == ('squirts\dialogs\date-picker-dialog.py'):
        try:
            from tkcalendar import Calendar
        except ImportError:
            messagebox.showwarning('Cannot run example:',
                                   'You need to pip install tkcalendar\n'
                                   'for this example to work.')
            return


    ask_yn = messagebox.askyesno('Question', 'Run example?')
    if ask_yn:
        webbrowser.open(py_file)

def pasted_info():
    """Pop up explains example code has been copied to clipboard."""
    messagebox.showinfo('Code copied',
                        'The code for your selection has been copied\n'
                        'to the clipboard.\n\nYou can paste '
                        'this straight into your\ncode editor '
                        'and it should work.')

def get_source_code(source_file):
    """Copy simple button example code to clipboard."""
    pyperclip.copy('') # Clear clipboard.
    # Open py file,(passed into this function) as text.
    with open(source_file, 'r') as contents:
        squirt_code = contents.read()

        pyperclip.copy(squirt_code) # Copy code to clipboard.
        pasted_info() # Pop up message.
        ask_execute(source_file) # Execute code example?


# Main gui combobox calls.

def combo_buttons():
    """Buttons combo menu."""
    sel_item = btns_combo.get()
    if sel_item == 'BUTTONS':
        return

    if sel_item == 'Simple Button':
        get_source_code(r'squirts\buttons\simple-button.py')

    if sel_item == 'Check Buttons':
        get_source_code(r'squirts\buttons\check-buttons.py')

    if sel_item == 'Radio Buttons':
        get_source_code(r'squirts\buttons\radio-buttons.py')

    if sel_item == 'Menu Button':
        get_source_code(r'squirts\buttons\menu-button.py')

    if sel_item == 'Image Button':
        get_source_code(r'squirts\buttons\image-button.py')

def combo_boxes():
    """Main gui, boxes combo."""
    sel_item = boxes_combo.get()
    if sel_item == 'BOXES':
        return
    if sel_item == 'Entry Box':
        get_source_code(r'squirts\boxes\entry-box.py')

    if sel_item == 'List Box':
        get_source_code(r'squirts\boxes\list-box.py')

    if sel_item == 'Combo Box':
        get_source_code(r'squirts\boxes\combo-box.py')

    if sel_item == 'Spin Box':
        get_source_code(r'squirts\boxes\spin-box.py')

    if sel_item == 'Scr Txt Box':
        get_source_code(r'squirts\boxes\scrolled-text-box.py')


def ask_msgboxes():
    """Main gui, ask msgbox combo."""
    sel_item = askmsg_boxes_combo.get()
    if sel_item == 'ASK MSG BOXES':
        return

    if sel_item == 'AskOkCancel':
        get_source_code(r'squirts\ask-msg-boxes\askokcancel-msg-box.py')

    if sel_item == 'AskRetryCancel':
        get_source_code(r'squirts\ask-msg-boxes\askretrycancel-msg-box.py')

    if sel_item == 'AskYN':
        get_source_code(r'squirts\ask-msg-boxes\askyn-msg-box.py')

    if sel_item == 'AskYNCancel':
        get_source_code(r'squirts\ask-msg-boxes\askyncancel-msg-box.py')

    if sel_item == 'Custom msg box':
        get_source_code(r'squirts\ask-msg-boxes\custom-msg-box.py')

def info_msgboxes():
    """Main gui, info msgbx combo."""
    sel_item = info_boxes_combo.get()
    if sel_item == 'INFO BOXES':
        return

    if sel_item == 'Info MsgBox':
        get_source_code(r'squirts\info-boxes\info-msg-box.py')

    if sel_item == 'Error MsgBox':
        get_source_code(r'squirts\info-boxes\error-msg-box.py')

    if sel_item == 'Warning MsgBox':
        get_source_code(r'squirts\info-boxes\warning-msg-box.py')
        return

def misc():
    """Main gui, misc combo."""
    sel_item = misc_combo.get()
    if sel_item == 'MISC':
        return

    if sel_item == 'Clock':
        get_source_code(r'squirts\misc\date-clock.py')

    if sel_item == 'Colour sliders':
        get_source_code(r'squirts\misc\colour-sliders.py')

    if sel_item == 'Progress Bar':
        get_source_code(r'squirts\misc\progress-bar.py')

    if sel_item == 'Display Image':
        get_source_code(r'squirts\misc\display-image.py')

    if sel_item == 'Lambda Callback':
        get_source_code(r'squirts\misc\lambda-callback.py')

    if sel_item == 'Simple Label':
        get_source_code(r'squirts\misc\simple-label.py')

    if sel_item == 'Simple scale':
        get_source_code(r'squirts\misc\simple-scale.py')

    if sel_item == 'Tool-Tips':
        get_source_code(r'squirts\misc\tool-tips.py')

    if sel_item == 'Vertical Scale':
        get_source_code(r'squirts\misc\vertical-scale.py')

def dialogs():
    """Main gui file dialogs."""
    sel_item = dialogs_combo.get()
    if sel_item == 'DIALOGS':
        return

    if sel_item == 'Ask Directory':
        get_source_code(r'squirts\dialogs\ask-directory-dialog.py')

    if sel_item == 'Color Picker':
        get_source_code(r'squirts\dialogs\color-picker-dialog.py')

    if sel_item == 'Date Picker':
        get_source_code(r'squirts\dialogs\date-picker-dialog.py')

    if sel_item == 'Open File':
        get_source_code(r'squirts\dialogs\open-file-dialog.py')

    if sel_item == 'Save File':
        get_source_code(r'squirts\dialogs\save-file-dialog.py')

    if sel_item == 'User Input':
        get_source_code(r'squirts\dialogs\user-input-dialog.py')

def menu():
    """Main gui menu calls."""
    sel_item = menu_combo.get()
    if sel_item == 'MENU':
        return

    if sel_item == 'Drop-down Menu':
        get_source_code(r'squirts\menu\drop-down-menu.py')

    if sel_item == 'Menu Check-marks':
        get_source_code(r'squirts\menu\menu-check-marks.py')

    if sel_item == 'Right-click Context Menu':
        get_source_code(r'squirts\menu\right-click-context-menu.py')

    if sel_item == 'Smart Option Menu':
        get_source_code(r'squirts\menu\smart-option-menu.py')

    if sel_item == 'Toolbar with Icons':
        get_source_code(r'squirts\menu\toolbar.py')


def window():
    """Main gui window calls."""
    sel_item = wndw_combo.get()
    if sel_item == 'WINDOW':
        return

    if sel_item == 'Centre Window':
        get_source_code(r'squirts\window\centre-window.py')

    if sel_item == 'Message Window':
        get_source_code(r'squirts\window\message-window.py')

    if sel_item == 'Paned Windows':
        get_source_code(r'squirts\window\paned-windows.py')

    if sel_item == 'Status Bar':
        get_source_code(r'squirts\window\status-bar.py')

    if sel_item == 'Tabbed Windows':
        get_source_code(r'squirts\window\tabbed-windows.py')

    if sel_item == 'Window Icon':
        get_source_code(r'squirts\window\window-icon.py')

# Drop-down menu.
menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Menu', menu=file_menu)
file_menu.add_command(label='Quick start help', command=quick_help)
file_menu.add_command(label='Online Help Page', command=help_page)
file_menu.add_separator()
file_menu.add_command(label='About program', command=about_menu)
file_menu.add_command(label='Visit my Python blog', command=visit_blog)
file_menu.add_command(label='Contact me', command=contact_me)
file_menu.add_separator()
file_menu.add_command(label='View squirts Folder', command=open_folder)
file_menu.add_separator()
file_menu.add_command(label='Tkinter Documentation', command=tk_docs)
file_menu.add_command(label='YouTube Tkinter Tutorials', command=ytube_tuts)
file_menu.add_command(label='Reddit ask for help', command=go_reddit)
file_menu.add_command(label='Python GUI Forum', command=python_forum)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=exit_app)
root.config(menu=menu_bar)

# Create inner labelframe.
combo_frame = LabelFrame(root, relief=RIDGE,
                         text='Please Select an item from the drop-down boxes')
combo_frame.grid(padx=20, pady=1, column=1, row=1)

# Combo boxes for main gui.
askmsg_boxes_combo = Combobox(combo_frame)
askmsg_boxes_combo['values'] = ('ASK MSG BOXES', 'AskOkCancel',
                                'AskRetryCancel', 'AskYNCancel', 'AskYN',
                                'Custom msg box')
askmsg_boxes_combo.current(0)
askmsg_boxes_combo.grid(row=0, column=0, padx=5, pady=5)
askmsg_btn = Button(combo_frame, bg='springgreen', text='Get', command=ask_msgboxes)
askmsg_btn.grid(row=0, column=1, sticky=W, padx=5, pady=5)
#---------------

boxes_combo = Combobox(combo_frame)
boxes_combo['values'] = ('BOXES', 'Combo Box', 'Entry Box', 'List Box',
                         'Scr Txt Box', 'Spin Box')
boxes_combo.current(0)
boxes_combo.grid(row=1, column=0, padx=5, pady=5)
boxes_btn = Button(combo_frame, bg='gold', text='Get', command=combo_boxes)
boxes_btn.grid(row=1, column=1, sticky=W, padx=5, pady=5)
#---------------
btns_combo = Combobox(combo_frame)
btns_combo['values'] = ('BUTTONS',
                        'Check Buttons', 'Image Button', 'Menu Button',
                        'Radio Buttons', 'Simple Button')
btns_combo.current(0)
btns_combo.grid(row=2, column=0, padx=5, pady=5)
btns_btn = Button(combo_frame, bg='salmon', text='Get', command=combo_buttons)
btns_btn.grid(row=2, column=1, sticky=W, padx=5, pady=5)

#---------------
dialogs_combo = Combobox(combo_frame)
dialogs_combo['values'] = ('DIALOGS', 'Ask Directory', 'Color Picker',
                           'Date Picker', 'Open File', 'Save File',
                           'User Input')
dialogs_combo.current(0)
dialogs_combo.grid(row=3, column=0, padx=5, pady=5)
dialogs_btn = Button(combo_frame, bg='red', text='Get', command=dialogs)
dialogs_btn.grid(row=3, column=1, sticky=W+E, padx=5, pady=5)
#---------------

info_boxes_combo = Combobox(combo_frame)
info_boxes_combo['values'] = ('INFO BOXES', 'Error MsgBox', 'Info MsgBox',
                              'Warning MsgBox')
info_boxes_combo.current(0)
info_boxes_combo.grid(row=0, column=2, padx=5, pady=5)
info_btn = Button(combo_frame, bg='plum', text='Get', command=info_msgboxes)
info_btn.grid(row=0, column=3, sticky=W+E, padx=5, pady=5)

#---------------
menu_combo = Combobox(combo_frame)
menu_combo['values'] = ('MENU', 'Drop-down Menu', 'Menu Check-marks',
                        'Right-click Context Menu', 'Smart Option Menu',
                        'Toolbar with Icons')
menu_combo.current(0)
menu_combo.grid(row=1, column=2, padx=5, pady=5)
menu_btn = Button(combo_frame, bg='yellow', text='Get', command=menu)
menu_btn.grid(row=1, column=3, sticky=W+E, padx=5, pady=5)

#---------------
misc_combo = Combobox(combo_frame)
misc_combo['values'] = ('MISC', 'Clock', 'Colour sliders', 'Display Image',
                        'Lambda Callback', 'Progress Bar', 'Simple Label',
                        'Simple scale', 'Tool-Tips', 'Vertical Scale')
misc_combo.current(0)
misc_combo.grid(row=2, column=2, padx=5, pady=5)
misc_btn = Button(combo_frame, bg='orange', text='Get', command=misc)
misc_btn.grid(row=2, column=3, sticky=W+E, padx=5, pady=5)
#---------------

wndw_combo = Combobox(combo_frame)
wndw_combo['values'] = ('WINDOW', 'Centre Window', 'Message Window',
                        'Paned Windows', 'Status Bar', 'Tabbed Windows',
                        'Window Icon')
wndw_combo.current(0)
wndw_combo.grid(row=3, column=2, padx=5, pady=5)
wndw_btn = Button(combo_frame, bg='skyblue', text='Get', command=window)
wndw_btn.grid(row=3, column=3, sticky=W+E, padx=5, pady=5)
#---------------

root.mainloop()
