import os
import time
import atrcopy
import tkinter as tk
from tkinter import font
import tkinter.ttk as ttk
from PIL import ImageTk, Image
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename

global filepath
filepath = None

global selected
selected = False

global convertedfile
convertedfile = None

# New file
def new_file():
    global filepath
    txt_edit.delete('1.0', 'end')
    filepath = None

# Open file
def open_file(e):
    """Open a file for editing."""
    global filepath
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    try:
        txt_edit.delete(1.0, tk.END)
        with open(filepath, "r") as input_file:
            text = input_file.read()
            txt_edit.insert(tk.END, text)
        window.title(f"MakeAD3B - {filepath}")
    except FileNotFoundError:
        return

# Save file
def save_file(e):
    """Save the current file as a new file."""
    global filepath
    if filepath is None:
        filepath = asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
    try:
        with open(filepath, "w") as output_file:
            text = txt_edit.get(1.0, tk.END)
            output_file.write(text)
        window.title(f"MakeAD3B - {filepath}")
    except FileNotFoundError:
        return

# Save file as
def save_file_as(e):
    """Save the current file as a new file."""
    global filepath
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")] 
    )
    try:
        save_file(e)
        window.title(f"MakeAD3B - {filepath}")
    except FileNotFoundError:
        return

# Convert txt file to dsk containing Applsoft BASIC commands (saved as a txt file)
def convert2basic():
    """Save the current file as an dsk image containing a text file."""
    global filepath
    global convertedfile
    if filepath is None:
        return
    
    if filepath is not None:
        convertedfile = asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        try:
            with open(filepath, "w") as output_file:
                text = txt_edit.get(1.0, tk.END)
                output_file.write(text[0:-1])
            with open(filepath, "r") as f:
                lines = f.readlines()
                n=0
                for i in range(len(lines)):
                    n+=10
                    if lines[i].startswith('>'):
                        lines[i] = '{} INPUT "";T$\n{} INPUT "";T$\n'.format(n,n+10)
                        n+=10
                    else:
                        lines[i] = '{} PRINT "{}"\n'.format(n,lines[i][:-1].upper())
            with open(convertedfile, 'w') as f1:
                for line in lines:
                    f1.write(line)
            
            cfile = convertedfile.split('/')[-1][0:-4]
            cfiledir = '\\'.join(convertedfile.split('/')[0:-1])
            
            os.chdir(cfiledir)
            os.system('atrcopy {}.dsk create -f dos33.dsk'.format(cfile))
            time.sleep(2)
            os.system('atrcopy {}.dsk add -f -t T {}.TXT'.format(cfile,cfile.upper()))
            
            progbar()

            if showconvtxt.get() == True:
                with open(convertedfile, 'r') as f2:
                  txt_edit.delete(1.0, tk.END)
                  text = f2.read()
                  txt_edit.insert(tk.END, text)

            if delconvfile.get() == True:
                try:
                    os.remove('{}.TXT'.format(cfile))
                except OSError:
                    return

            showinfo('MakeAD3B', 'File successfully converted.')
            window.title(f"MakeAD3B - {convertedfile}")
        except FileNotFoundError:
            return

# Dummy progress bar
def progbar():
    #start progress bar
    size = range(100)
    popup = tk.Toplevel()
    popup.rowconfigure(0, minsize=30, weight=1)
    popup.columnconfigure(0, minsize=180, weight=1)
    tk.Label(popup, text="File being converted...").grid(row=0,column=0)

    progress = 0
    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(popup, variable=progress_var, maximum=100)
    progress_bar.grid(row=1, column=0, pady=5.0)
    popup.pack_slaves()

    progress_step = float(100.0/len(size))
    for _ in size:
        popup.update()
        time.sleep(0.1)
        progress += progress_step
        progress_var.set(progress)
    popup.destroy()

# Cut text
def cut_text(e):
    global selected
    if e:
        selected = window.clipboard_get()
    elif txt_edit.selection_get():
        selected = txt_edit.selection_get()
        txt_edit.delete('sel.first','sel.last')
        window.clipboard_clear()
        window.clipboard_append(selected)

# Copy text
def copy_text(e):
    global selected
    if e:
        selected = window.clipboard_get()
    if txt_edit.selection_get():
        selected = txt_edit.selection_get()
        window.clipboard_clear()
        window.clipboard_append(selected)

# Paste text
def paste_text(e):
    global selected
    if e:
        selected = window.clipboard_get()
    elif selected:
        position = txt_edit.index(tk.INSERT)
        txt_edit.insert(position,selected)

# About info
def aboutinfo(e):
    showinfo('MakeAD3B by DJRemedyMusic', 'MakeAD3B is a Python text editor and conversion program (made by DJRemedyMusic) that takes a dialogue script and converts it into a DOS3.3 disk image containing a text file with a series of Applsoft Basic commands which will be used to type your dialogue as if it were Deb herself responding to you.')

# Project 863 themed themes
def SyphusMode(e):
    main_color = '#000000'
    secondary_color = '#373737'
    txt_color = '#33ff00'
    
    window.iconbitmap(os.path.dirname(os.path.abspath(__file__))+"/images/Logo_Final_Happy_copy.ico")
    window.config(bg=secondary_color)
    my_frame.config(bg=secondary_color)
    status_bar.config(bg=secondary_color,fg=txt_color)
    txt_edit.config(bg=main_color,fg=txt_color,insertbackground=txt_color)
    fr_buttons.config(bg=secondary_color)
    btn_c2b.config(bg=txt_color,fg=main_color)
    file_menu.config(bg=main_color,fg=txt_color)
    edit_menu.config(bg=main_color,fg=txt_color)
    help_menu.config(bg=main_color,fg=txt_color)
    theme_menu.config(bg=main_color,fg=txt_color)

def SyntecMode(e):
    main_color = 'SystemButtonFace'
    secondary_color = 'SystemButtonFace'
    txt_color = '#000000'

    window.iconbitmap(os.path.dirname(os.path.abspath(__file__))+"/images/Syntec_logo.ico")
    window.config(bg=secondary_color)
    my_frame.config(bg=secondary_color)
    status_bar.config(bg=secondary_color,fg=txt_color)
    txt_edit.config(bg='#ffffff',fg=txt_color,insertbackground=txt_color)
    fr_buttons.config(bg=secondary_color)
    btn_c2b.config(bg='#56c1c1',fg=txt_color)
    file_menu.config(bg=main_color,fg=txt_color)
    edit_menu.config(bg=main_color,fg=txt_color)
    help_menu.config(bg=main_color,fg=txt_color)
    theme_menu.config(bg=main_color,fg=txt_color)

if __name__ == '__main__':
    # Create window instance
    window = tk.Tk()
    window.iconbitmap(os.path.dirname(os.path.abspath(__file__))+"/images/Syntec_logo.ico")
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    app_width = int(screen_width/2)
    app_height = int(screen_height/2)
    x = (screen_width/2) - (app_width/2)
    y = (screen_height/2) - (app_height/2)
    window.title("MakeAD3B")
    window.rowconfigure(0, minsize=800,weight=1)
    window.columnconfigure(0, minsize=800,weight=1)
    window.geometry('{}x{}+{}+{}'.format(app_width,app_height,int(x),int(y)))

    # Create Boolean vars for Options menu
    showconvtxt = tk.BooleanVar()
    showconvtxt.set(False)

    delconvfile = tk.BooleanVar()
    delconvfile.set(False)
    
    # Create a frame
    my_frame = tk.Frame(window)
    my_frame.pack(side=tk.BOTTOM,pady=5,ipadx=app_width)
    
    # Create vertical scrollbar
    vscroll_bar = tk.Scrollbar(window)
    vscroll_bar.pack(side=tk.RIGHT,fill=tk.Y)

    # Create horizontal scrollbar
    hscroll_bar = tk.Scrollbar(window, orient=tk.HORIZONTAL)
    hscroll_bar.pack(side=tk.BOTTOM, fill=tk.X)

    # Create text box
    txt_edit = tk.Text(window, undo=True, maxundo=-1, autoseparators=True, font=("Courier New", 12), selectbackground='#5495fe',selectforeground='white',yscrollcommand=vscroll_bar.set, wrap='none',xscrollcommand=hscroll_bar.set)
    txt_edit.pack(fill=tk.BOTH, expand=True)

    # Configure scrollbars
    vscroll_bar.config(command=txt_edit.yview)
    hscroll_bar.config(command=txt_edit.xview)

    # Make main menu
    mymenu = tk.Menu(window)
    window.config(menu=mymenu)
    
    # Add file menu
    file_menu = tk.Menu(mymenu,tearoff=False)
    mymenu.add_cascade(label='File',menu=file_menu)
    file_menu.add_command(label='New File',accelerator='Ctrl+N',command=lambda: new_file(False))
    file_menu.add_separator()
    file_menu.add_command(label='Open File...',accelerator='Ctrl+O',command=lambda: open_file(False))
    file_menu.add_separator()
    file_menu.add_command(label='Save',accelerator='Ctrl+S',command=lambda: save_file(False))
    file_menu.add_command(label='Save as...',accelerator='Ctrl+Shift+S',command=lambda: save_file_as(False))
    file_menu.add_separator()
    file_menu.add_command(label='Exit',command=window.quit)
    
    # Add edit menu
    edit_menu = tk.Menu(mymenu,tearoff=False)
    mymenu.add_cascade(label='Edit',menu=edit_menu)
    edit_menu.add_command(label='Undo',accelerator='Ctrl+Z', command=txt_edit.edit_undo)
    edit_menu.add_command(label='Redo',accelerator='Ctrl+Y',command=txt_edit.edit_redo)
    edit_menu.add_separator()
    edit_menu.add_command(label='Cut', accelerator='Ctrl+X', command=lambda: cut_text(False))
    edit_menu.add_command(label='Copy', accelerator='Ctrl+C', command=lambda: copy_text(False))
    edit_menu.add_command(label='Paste', accelerator='Ctrl+V', command=lambda: paste_text(False))
    
    # Add options menu with themes submenu
    options_menu = tk.Menu(mymenu,tearoff=False)
    theme_menu = tk.Menu(options_menu,tearoff=False)
    mymenu.add_cascade(label='Options',menu=options_menu)
    options_menu.add_cascade(label='Themes',menu=theme_menu)
    theme_menu.add_command(label='Syntec Theme (Light Mode)', command=lambda: SyntecMode(False))
    theme_menu.add_command(label='Syphus Theme (Dark Mode)', command=lambda: SyphusMode(False))
    options_menu.add_checkbutton(label='Show Converted Text', onvalue=1, offvalue=0, variable=showconvtxt)
    options_menu.add_checkbutton(label='Delete Temporary Converted TXT File', onvalue=1, offvalue=0, variable=delconvfile)

    # Add help menu
    help_menu = tk.Menu(mymenu,tearoff=False)
    mymenu.add_cascade(label='Help',menu=help_menu)
    help_menu.add_command(label='About', command=lambda: aboutinfo(False))
    
    # Create convert button
    fr_buttons = tk.Frame(my_frame, padx=5)
    fr_buttons.pack(side=tk.TOP)
    btn_c2b = tk.Button(fr_buttons, text="Convert", command=convert2basic, bg='#56c1c1',fg='#000000')
    btn_c2b.pack(side=tk.TOP, anchor=tk.N)
    
    # Edit Bindings
    window.bind('<Control-Key-n>', new_file)
    window.bind('<Control-Key-o>', open_file)
    window.bind('<Control-Key-s>', save_file)
    window.bind('<Control-Shift-s>', save_file_as)
    window.bind('<Control-Key-x>', cut_text)
    window.bind('<Control-Key-c>', copy_text)
    window.bind('<Control-Key-v>', paste_text)

    # Create status bar
    var = tk.StringVar()
    status_bar = tk.Label(my_frame, textvariable=var, anchor=tk.E)
    var.set('Ready    ')
    status_bar.pack(side=tk.BOTTOM, fill=tk.X, ipady=5)

    window.mainloop()