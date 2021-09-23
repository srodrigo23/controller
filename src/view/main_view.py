import tkinter as tk
from tkinter import Frame, LabelFrame

from .server_panel import ServerPanel
from .frame_monitor import FrameMonitor

class MainView(tk.Tk):

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.num_cams = self.controller.num_cams
        self.setup()
        self.setup_server_panel()
        self.setup_panel_cameras()
            
    def setup(self):
        self.title("CLIENT")
        self.container = Frame(self, bg=self.controller.settings.get_bg_color())
        self.set_dimension(800, 520)
        self.container.pack(side='top', fill='both', expand=True)
        
    def setup_server_panel(self):
        self.server_panel = ServerPanel(
            self.container, self.controller, text='SERVER')
        self.server_panel.pack(side='right', fill='both', expand=1, padx=5, pady=5)
    
    def setup_panel_cameras(self):
        self.monitors = LabelFrame(self.container,
                                   text="CAMERAS",
                                   bg=self.controller.settings.get_bg_color())

        mnt1 =  FrameMonitor(self.monitors, self.controller, id_camera=0, text= "NODE 1")
        mnt1.pack(side='top', fill='both', expand=1, padx=5, pady=5)
        
        mnt2 = FrameMonitor(self.monitors, self.controller, id_camera=1, text= "NODE 2")
        mnt2.pack(side='top', fill='both', expand=1, padx=5, pady=5)
        
        self.monitors.pack(side='left', fill='x', padx=5, pady=5)
    
    def set_dimension(self, w_width, w_height):
        pos_top = int(self.winfo_screenheight()/2 - w_height/2) 
        pos_right = int(self.winfo_screenwidth()/2 - w_width/2)
        self.geometry(f'{w_width}x{w_height}+{pos_right}+{pos_top}')