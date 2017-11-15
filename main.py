# Importing Tkinter module
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


# Following Structured-Oriented thoughts, so we have to split the whole code into functions.

def main():

    def do_nothing():
        x = 0

    def fullscreen():
        root.attributes('-fullscreen', True)

    def exit_full_screen():
        root.attributes('-fullscreen', False)

    def import_fasta_file():
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",filetypes=(("Fasta Files", "*.fasta"),("All Files", "*.*")))
        print(root.filename)

    def import_excel_file():
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",filetypes=(("Excel files", "*.xlsx"),("All Files", "*.*")))
        print(root.filename)

    def ask_quit():
        if messagebox.askokcancel("EXIT","Are You Sure?"):
            root.quit()

    def create_window():
       new_window = Toplevel(root)
       return new_window

    root = Tk()

    w = 800
    h = 650
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.title('DNA_Motif_PKG V1.01')

    menubar = Menu(root)
    root.config(menu=menubar)

    filemenu = Menu(menubar,tearoff=0)
    menubar.add_cascade(label="File",menu=filemenu)
    filemenu.add_command(label="New Window",command=create_window)
    filemenu.add_command(label="Import Fasta File",command=import_fasta_file)
    filemenu.add_command(label="Import Excel File",command=import_excel_file)
    filemenu.add_separator()
    filemenu.add_command(label="Save File",command=do_nothing)
    filemenu.add_separator()
    filemenu.add_command(label="Exit",command=ask_quit)

    editmenu = Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Edit",menu=editmenu)
    editmenu.add_command(label="Undo",command=do_nothing)
    editmenu.add_command(label="Redo",command=do_nothing)

    viewmenu = Menu(menubar,tearoff=0)
    menubar.add_cascade(label="View",menu=viewmenu)
    viewmenu.add_command(label="Normal Size",command=exit_full_screen)
    viewmenu.add_command(label="Full Screen",command=fullscreen)

    runmenu = Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Run",menu=runmenu)
    runmenu.add_command(label="Motif Count",command=do_nothing)
    runmenu.add_command(label="X Clustering",command=do_nothing)
    runmenu.add_command(label="Y Clustering",command=do_nothing)

    helpmenu = Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Help",menu=helpmenu)
    helpmenu.add_command(label="How To Use?",command=do_nothing)
    helpmenu.add_command(label="About Fasta File")
    helpmenu.add_command(label="About Us")

    root.protocol("WM_DELETE_WINDOW", ask_quit)

    root.mainloop()


main()
