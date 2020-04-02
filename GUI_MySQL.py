import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg


class OOP:
    def __init__(self):
        # Create instance
        self.win = tk.Tk()

        # Add a title
        self.win.title('Python GUI')
        self.create_widgets()

    # Modified Button Click Event callback Function - Now a method in the OOP class
    def insert_quote(self):
        pass

    def get_quotes(self):
        pass

    def modify_quote(self):
        pass

    # Exit GUI cleanly
    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()

    def create_widgets(self):
        # Create Tab Control
        tabControl = ttk.Notebook(self.win)  # Create Tab Control
        tab1 = ttk.Frame(tabControl)  # Create the first tab using the Frame class
        tabControl.add(tab1, text='MySQL')  # Adding the tab to the tabControl
        tab2 = ttk.Frame(tabControl)  # Create second tab
        tabControl.add(tab2, text='Widgets')  # Add second tab to the tabControl
        tabControl.pack(expand=1, fill='both')  # Pack the tabControl and tabs into the main GUI form to make visible
        # LabelFrame using tab1 as the parent
        mighty = ttk.LabelFrame(tab1, text=' Python Database ')
        mighty.grid(column=0, row=0, padx=8, pady=4)
        book_qte = ttk.LabelFrame(tab1, text=' Book Quotation ')
        book_qte.grid(column=0, row=1, padx=8, pady=4)
        # LabelFrame using tab2 as the parent
        self.mighty2 = ttk.LabelFrame(tab2, text=' The Snake ')
        self.mighty2.grid(column=0, row=0, padx=8, pady=4)
        # Modify adding a Label using mighty as the parent instead of win
        a_label = ttk.Label(mighty, text="Book Title:")
        a_label.grid(column=0, row=0, sticky='W')
        page_label = ttk.Label(mighty, text='Page:')
        page_label.grid(column=1, row=0, sticky=tk.W)

        # Adding three Text box Entry widget/ Text Entry Box
        self.name = tk.StringVar()
        self.title2 = tk.StringVar()
        self.title3 = tk.StringVar()
        self.name_entered = ttk.Entry(mighty, width=40, textvariable=self.name)
        self.name_entered.grid(column=0, row=1, sticky=tk.W, padx=2, pady=3)
        self.title2_entered = ttk.Entry(mighty, width=40, textvariable=self.title2)
        self.title2_entered.grid(column=0, row=2, sticky=tk.W, padx=2, pady=3)
        self.title3_entered = ttk.Entry(mighty, width=40, textvariable=self.title3)
        self.title3_entered.grid(column=0, row=3, sticky=tk.W, padx=2, pady=3)
        # Adding three entry widgets for page number
        self.page1 = tk.IntVar().set('')
        self.page2 = tk.IntVar().set('')
        self.page3 = tk.IntVar().set('')
        # for val in vars((self.page1, self.page2, self.page3)).values():
        #                     val.set('')
        self.page1_ent = ttk.Entry(mighty, width=3, textvariable=self.page1)
        self.page1_ent.grid(column=1, row=1, sticky=tk.W, padx=2, pady=3)
        self.page2_ent = ttk.Entry(mighty, width=3, textvariable=self.page2)
        self.page2_ent.grid(column=1, row=2, sticky=tk.W, padx=2, pady=3)
        self.page3_ent = ttk.Entry(mighty, width=3, textvariable=self.page3)
        self.page3_ent.grid(column=1, row=3, sticky=tk.W, padx=2, pady=3)
        # Adding three Buttons
        self.action = ttk.Button(mighty, text="Insert Quote", command=self.insert_quote)
        self.action.grid(column=2, row=1, padx=2, pady=3)
        self.action2 = ttk.Button(mighty, text="Get Quotes", command=self.get_quotes)
        self.action2.grid(column=2, row=2, padx=2, pady=3)
        self.action3 = ttk.Button(mighty, text="Modify Quote", command=self.modify_quote)
        self.action3.grid(column=2, row=3, padx=2, pady=3)

        # using a scrolled Text Control
        scroll_w = 50
        scroll_h = 7
        self.scr = scrolledtext.ScrolledText(book_qte, width=scroll_w, height=scroll_h, wrap=tk.WORD)
        self.scr.grid(column=0, row=0, sticky=tk.EW)

        # Creating a Menu Bar
        menu_bar = Menu(self.win)
        self.win.config(menu=menu_bar)

        # Create menu and add menu items
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label='New')
        # Adding a separate line
        file_menu.add_separator()
        # Add new item to the menu
        file_menu.add_command(label='Exit', command=self._quit)

        # Add file_menu(i.e menu) to menu bar and give it a label
        menu_bar.add_cascade(label='File', menu=file_menu)

        # Display a Message Box
        def _msgBox():
            answer = msg.askyesnocancel('Python Message Multi Choice Box', 'Are you sure you really wish to do this')
            print(answer)

        # Add another Menu to the Menu bar and an item
        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label='About', command=_msgBox)
        menu_bar.add_cascade(label='Help', menu=help_menu)

        # Change the main windows icon
        self.win.iconbitmap('pyc.ico')

        self.name_entered.focus()  # Place cursor into name Entry
    # ==========================================================
    # Start GUI
    # ==========================================================
    # Loop GUI to appear to end-user


oop = OOP()  # create an instance of the class
oop.win.mainloop()
