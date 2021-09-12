import tkinter as tk
from tkinter.ttk import Button
from tkinter import LabelFrame, Label

class ServerPanel(LabelFrame):
    
    def __init__(self, parent, controller, text):
        tk.LabelFrame.__init__(self, parent, text=text, bg=controller.settings.get_bg_color())
        self.controller = controller
        self.clock_label = Label(self, font=('times', 18, 'bold'), 
                                 bg=controller.settings.get_bg_color(), fg='red')
        self.clock_label.pack(side='left',padx=5, pady=5)
        self.change_time()
        self.add_buttons()
        
        self.turned_on = False
    
    def action(self):
        if not self.turned_on:
            self.controller.run_server()
            self.turned_on = True
            self.switch_server.configure(text="Apagar")
        else:
            self.controller.kill_server()
            self.turned_on = False
            self.switch_server.configure(text="Encender")
            
    def add_buttons(self):
        # print(self.controller.settings.get_btn_on_color())
        self.switch_server = Button(
            self, text='Encender', command=self.action, width=10
            # bg=self.controller.settings.get_btn_on_color()
            )
        self.switch_server.pack(side='left'
                                    #  , padx=5, pady=5
                                     )
        self.connect_server = Button(self, text='Conectar', width=10)
        self.connect_server.pack(side='left')
        
    def change_time(self):
        self.clock_label.config(text=self.controller.get_time())
        self.clock_label.after(1000, self.change_time)
    
    def set_time(self):
        self.clock_label.config(text=self.get_time())
