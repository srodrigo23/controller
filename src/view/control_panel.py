import tkinter as tk
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
        
    def change_time(self):
        self.clock_label.config(text=self.controller.get_time())
        self.clock_label.after(1000, self.change_time)
    
    def set_time(self):
        self.clock_label.config(text=self.get_time())