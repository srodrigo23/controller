import tkinter as tk

from tkinter.ttk import Button
from tkinter import LabelFrame, Label

class ControlPanel(LabelFrame):
    
    def __init__(self, parent, controller, text):
        tk.LabelFrame.__init__(self, parent, text=text)
        self.controller = controller
        self.clock_label= Label(self, 
                                font=('times', 18, 'bold'), 
                                bg='green', fg='white')
        self.clock_label.pack(side='left',padx=5, pady=5)
        self.change_time()
        self.add_buttons()
        
        self.turned_on = False
    
    def action(self):
        if not self.turned_on:
            self.controller.run_server()
            self.turned_on = True
            self.turn_on_off_server.configure(text="Apagar Servidor")
        else:
            self.controller.kill_server()
            self.turned_on = False
            self.turn_on_off_server.configure(text="Encender Servidor")
            
    def add_buttons(self):
        self.turn_on_off_server = Button(
            self, text='Encender servidor', compound='left', command=self.action)
        self.turn_on_off_server.pack(side='left', padx=5, pady=5)
        
    def change_time(self):
        self.clock_label.config(text=self.controller.get_time())
        self.clock_label.after(1000, self.change_time)
    
    def set_time(self):
        self.clock_label.config(text=self.get_time())
