import tkinter as tk
from tkinter import LabelFrame, Label
from tkinter import Frame
from tkinter import Canvas
from tkinter import Listbox

from tkinter.ttk import Button
from tkinter import PhotoImage
from tkinter.ttk import Scrollbar

import time
import PIL.Image, PIL.ImageTk

class View(tk.Tk):

    def __init__(self, model):
        super().__init__()
        self.title("Monitor de Camaras")

        self.container=Frame(self)
        self.container.pack(side='top', 
                            fill='both', 
                            expand=True)
        self.set_dimension(1000, 500)
        self.screens = []
        
        self.model = model
        
        self.control_panel = Control_Panel(self.container, text='Control Panel')
        self.control_panel.pack(side='top', fill='x', padx=5, pady=5)
        
        for i in range(3):
            num_camera = i+1
            self.screens.append(
                Frame_Camera(self.container, model, text=f'Camera {num_camera}'))
            self.screens[i].pack(
                side='left', 
                fill='both', 
                expand=1, 
                padx=5, pady=5)
        self.mainloop()

    def set_dimension(self, w_width, w_height):
        pos_top = int(self.winfo_screenheight()/2 - w_height/2) 
        pos_right = int(self.winfo_screenwidth()/2 - w_width/2)
        self.geometry(f'{w_width}x{w_height}+{pos_right}+{pos_top}')

class Control_Panel(LabelFrame):
    
    def __init__(self, parent, text):
        tk.LabelFrame.__init__(self, parent, text=text)
        self.clock_label= Label(self, 
                                font=('times', 18, 'bold'), 
                                bg='green', fg='white')
        self.clock_label.pack(side='left',padx=5, pady=5)
        self.change_time()

    def change_time(self):
        self.clock_label.config(text=self.get_time())
        self.clock_label.after(200, self.change_time)

    def get_time(self):
        return time.strftime('%H:%M:%S')
    
    
class Frame_Camera(LabelFrame):
    
    def __init__(self, parent, model, text):
        tk.LabelFrame.__init__(self, parent, text=text)
        
        self.model = model # this is the model
        
        self.monitor_animation = PhotoImage(file='../assets/tenor.gif')
        # To Do canvas dimensions
        self.monitor = Canvas(self, width=300,height=200)
        # self.monitor.create_image(0, 0, 
        #                           image=self.monitor_animation,anchor='nw')
            
        self.monitor.pack(side='top')
        self.set_button_launch_camera()
        self.set_button_turnoff_camera()
        self.set_list_videos(self, self.model.get_list_videos())
        self.update()
        
    
    # to changeeee
    def update(self): # Get a frame from the video source
        ret,frame = self.model.get_frame()
        if ret:
            self.picture = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.monitor.create_image(0, 0, image = self.picture, anchor = tk.NW)
            self.after(180, self.update)
            
    # def 

    def set_button_launch_camera(self):
        self.icon_turn_on = PhotoImage(file='../assets/turn_on.png')
        self.btn_turn_on = Button(self,
                                  image=self.icon_turn_on,
                                  compound='left',
                                  text='Encender Camara')
        self.btn_turn_on.pack(
            side='top',
            fill='x',
            padx=5, pady=5,
            expand=0
        )
    
    def set_button_turnoff_camera(self):
        self.icon_turn_off = PhotoImage(file='../assets/turn_off.png')
        self.btn_turn_off = Button(self,
                                  image=self.icon_turn_off,
                                  compound='left',
                                #   command=lamba,
                                  text='Apagar Camara')
        self.btn_turn_off.pack(
            side='top',
            fill='x',
            padx=5, pady=5,
            expand=0
        )
        
    def set_list_videos(self, parent, videos_list):
        scroll_bar = Scrollbar(parent, orient=tk.VERTICAL)
        self.videos_list = Listbox(parent, yscrollcommand=scroll_bar.set)
        self.videos_list['selectforeground'] = "#ffffff"
        self.videos_list['selectbackground']="#00aa00"
        self.videos_list['selectborderwidth'] = 1
        self.videos_list.configure(exportselection=False)
    
        self.videos_list.bind("<<ListboxSelect>>", self.mostrar_indice)

        for el in videos_list:
            self.videos_list.insert(tk.END, el)
            
        scroll_bar.config(command=self.videos_list.yview)
        scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
        self.videos_list.pack(expand=0, fill='x')
    
    def mostrar_indice(self, event):
        listbox = event.widget
        index = listbox.curselection()
        value = listbox.get(index[0])
        print(value)