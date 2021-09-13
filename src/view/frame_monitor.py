import tkinter as tk
import os
from tkinter import filedialog as fd
from tkinter.ttk import Scrollbar, Combobox, Button
from tkinter.messagebox import showinfo
from tkinter import PhotoImage, LabelFrame, Canvas, Listbox, Label, Frame
import PIL.Image, PIL.ImageTk

class FrameMonitor(LabelFrame):
    
    def __init__(self, parent, controller, id_camera, text):
        tk.LabelFrame.__init__(self, parent, text=text, 
                               bg = controller.settings.get_bg_color())
        self.controller = controller
        self.my_id = id_camera
        self.setup_monitor()
        self.setup_source_video()
        self.setup_controls()
        self.notifications()
        # self.setup_messages_list()
    
    def notifications(self):
        lbl_notif = LabelFrame(self, text="Notifications", bg=self.controller.settings.get_bg_color())
        lbl_notif.pack(side='left', fill='both', expand=1, padx=5, pady=5)
        
        lbl_notif.columnconfigure(0, weight=1)
        lbl_notif.columnconfigure(1, weight=1)
        
        lbl_fire = Label(lbl_notif, text='Fire',
                         bg=self.controller.settings.get_color_red())
        lbl_fire.grid(row=0, column=0, sticky='ew', padx=2, pady=2)
        
        lbl_violence = Label(lbl_notif, text='Violence',
                             bg=self.controller.settings.get_color_green())
        # lbl_violence.pack(fill='both')
        lbl_violence.grid(row=1, column=0, sticky='ew', padx=2, pady=2)
        
        lbl_outsider = Label(lbl_notif, text='Outsider',
                             bg=self.controller.settings.get_color_yellow())
        lbl_outsider.grid(row=0, column=1, sticky='ew', padx=2, pady=2)
        
        lbl_smoke = Label(lbl_notif, text='Smoke',
                          bg=self.controller.settings.get_color_lead())
        lbl_smoke.grid(row=1, column=1, sticky='ew', padx=2, pady=2)
        
        
        
    def setup_source_video(self):
        frm_source = LabelFrame(self, text="Source", bg=self.controller.settings.get_bg_color())
        videos, path = self.controller.get_videos()
        self.video_source = Combobox(frm_source, state='readonly', values=videos)
        self.video_source.current(0)
        self.video_source.pack(side='top', fill='x', padx=10)
        frm_source.pack(side='top', fill='x', expand=0, padx=5, pady=5)
    
    def setup_controls(self):
        frm_controls = LabelFrame(self, bg=self.controller.settings.get_bg_color())
        frm_controls.pack(side='top', fill='x', expand=0, padx=5, pady=5)
        
        self.btn_turn_on = Button(frm_controls, compound='left', text='Launch',
                                  command=self.launch_open_file)
        self.btn_turn_on.pack(side='left', fill='x', padx=5, pady=5, expand=1)
        
        lbl_frm_pid = LabelFrame(
            frm_controls, text='PID', bg=self.controller.settings.get_bg_color())
        lbl_frm_pid.pack(side='left', fill='x', expand=0)
        
        lbl_pid = Label(lbl_frm_pid, text='1234',
                        bg=self.controller.settings.get_bg_color(), font=("Helvetica", 18), fg="Red")
        lbl_pid.pack(side='left', fill='both', expand=1)
    
    
    def launch_open_file(self):
        path = os.path.sep.join([self.controller.settings.get_videos_path(), 
                                 self.video_source.get()])
        self.controller.launch_camera_process(path)
    
    def setup_monitor(self):
        self.status = "Offline"
        self.message = f"Status : - {self.status} - "
        frm_monitor = LabelFrame(self, text=self.message, bg=self.controller.settings.get_bg_color())
        self.monitor = Canvas(frm_monitor, width=320,height=180)
        self.monitor.pack(side='top', expand='1', fill='both')
        frm_monitor.pack(side='left', fill='x', padx='5', pady='5', expand='1')
        self.update_frame()
    
    def update_frame(self): # Get a frame from the video source
        frame = self.controller.get_frame(self.my_id)
        self.picture = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
        self.monitor.create_image(0, 0, image = self.picture, anchor = tk.NW)
        self.after(50, self.update_frame)
            
    def setup_label_title(self):
        self.label_title = Label(self)
        self.label_title.pack(side="top", fill="both", expand=True)

    def setup_messages_list(self):
        frm_list = LabelFrame(self, text="Mensajes")
        scroll_bar = Scrollbar(frm_list, orient=tk.VERTICAL)
        self.messages_list = Listbox(frm_list, yscrollcommand=scroll_bar.set)
        self.messages_list['selectforeground'] = "#ffffff"
        self.messages_list['selectbackground'] = "#00aa00"
        self.messages_list['selectborderwidth'] = 1
        self.messages_list.configure(exportselection=False)
        scroll_bar.config(command=self.messages_list.yview)
        scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
        self.messages_list.pack(expand=1, fill='both', padx=3)
        frm_list.pack(side='top', fill='both', expand=1, padx=5, pady=5)
        # self.messages_list.bind("<<ListboxSelect>>", self.mostrar_indice)
        
    def mostrar_indice(self, event):
        listbox = event.widget
        index = listbox.curselection()
        value = listbox.get(index[0])
        self.label_title.configure(text=value)
        
    def add_elements_list(self, videos_list):
        for el in videos_list:
            self.videos_list.insert(tk.END, el)
