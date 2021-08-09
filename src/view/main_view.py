import tkinter as tk
from tkinter import Frame

from .control_panel import ControlPanel
from .frame_camera import FrameCamera

class MainView(tk.Tk):

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.num_cams = self.controller.num_cams
        self.setup()
        self.setup_panel_control()
        self.setup_panel_cameras()
            
    def setup(self):
        self.title("Monitor de Cámaras")
        self.container = Frame(self)
        self.set_dimension(1400, 550)
        self.container.pack(side='top', fill='both', expand=True)
        
    def setup_panel_control(self):
        self.control_panel = ControlPanel(self.container, self.controller, text='Control Panel')
        self.control_panel.pack(side='top', fill='x', padx=5, pady=5)
    
    def setup_panel_cameras(self):
        self.panels_cameras = []
        for i in range(self.num_cams):
            num_camera = i+1
            self.panels_cameras.append(FrameCamera(self.container, self.controller,id_camera=i, text=f'Camera {num_camera}'))
            self.panels_cameras[i].pack(side='left', fill='both', expand=1, padx=5, pady=5)
    
    def set_dimension(self, w_width, w_height):
        pos_top = int(self.winfo_screenheight()/2 - w_height/2) 
        pos_right = int(self.winfo_screenwidth()/2 - w_width/2)
        self.geometry(f'{w_width}x{w_height}+{pos_right}+{pos_top}')