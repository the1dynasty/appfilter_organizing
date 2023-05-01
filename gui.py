import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from ttkthemes import ThemedStyle

class App:
    def __init__(self, master):
        self.master = master
        self.folder_path = ''
        
        # set Material Design style
        self.style = ThemedStyle(self.master)
        self.style.set_theme('equilux')

        self.master.title('Appfilter Organizer')
        self.master.geometry('400x200')

        # create header label
        self.header_label = ttk.Label(self.master, text='Appfilter Organizer', font=('Roboto', 24, 'bold'), anchor='center')
        self.header_label.pack(side='top', pady=(10, 20))

        # create select folder button
        self.folder_button = ttk.Button(self.master, text='Select Folder', command=self.select_folder, style='Accent.TButton')
        self.folder_button.pack(side='top', padx=20, pady=10, fill='x')

        # create run script button
        self.run_button = ttk.Button(self.master, text='Organize', command=self.run_script, state='disabled', style='Accent.TButton')
        self.run_button.pack(side='top', padx=20, pady=10, fill='x')

        # create status label
        self.status_label = ttk.Label(self.master, text='Select a folder to begin.', font=('Roboto', 12), anchor='center')
        self.status_label.pack(side='top', pady=20)

        # center everything vertically and horizontally
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_rowconfigure(4, weight=1)

        # bind enter key to run script button
        self.master.bind('<Return>', lambda event: self.run_script())

    def select_folder(self):
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            self.status_label.config(text='Folder selected: {}'.format(self.folder_path))
            self.run_button.config(state='normal')

    def run_script(self):
        script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'appfilter_script.py')
        os.system('python3 "{}" "{}"'.format(script_path, self.folder_path))
        self.status_label.config(text='Script complete.')
        self.run_button.config(state='disabled')

root = tk.Tk()
app = App(root)
root.mainloop()
