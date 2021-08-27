import tkinter as tk
from tkinter.ttk import Button, Scrollbar, Combobox
from tkinter import PhotoImage, LabelFrame, Canvas, Listbox, Label
import PIL.Image, PIL.ImageTk

class FrameCamera(LabelFrame):
    
    def __init__(self, parent, controller, id_camera, text):
        tk.LabelFrame.__init__(self, parent, text=text)
        self.controller = controller
        self.my_id = id_camera
        self.setup_monitor()
        self.setup_source_video()
        self.setup_buttons()
        self.setup_messages_list()
        
    def setup_source_video(self):
        frm_source = LabelFrame(self, text="Fuente")
        videos, path = self.controller.get_videos()
        self.video_source = Combobox(frm_source, 
                                     state='readonly', 
                                     values=videos)
        self.video_source.current(0)
        self.video_source.pack(side='top', 
                            #    fill='x', 
                               padx=10)
        frm_source.pack(side='top', 
                        # fill='both', 
                        expand=1, padx=5, pady=5)
    
    def setup_buttons(self):
        frm_buttons = LabelFrame(self, text="Controles")
        self.btn_turn_on = Button(frm_buttons, 
                                #   image=self.icon_turn_on, 
                                  compound='left', text='Encender')
        self.btn_turn_on.pack(side='left', fill='x', padx=5, pady=5, expand=1)
        self.btn_turn_off = Button(frm_buttons, 
                                #    image=self.icon_turn_off, 
                                   compound='left',text='Apagar',
                                #    command=self.controller.change_time()
                                   )
        self.btn_turn_off.pack(side='left', fill='x',padx=5, pady=5, expand=1)
        frm_buttons.pack(side='top', fill='both', expand=1, padx=5, pady=5)
        
    def setup_monitor(self):
        self.status = "Fuera de linea"
        self.message = f"Estado : - {self.status} - "
        frm_monitor =  LabelFrame(self, text=self.message)
        self.monitor = Canvas(frm_monitor, width=320,height=180)
        self.monitor.pack(side='top', expand='1', fill='both')
        frm_monitor.pack(side='top', fill='both', padx='5', pady='5', expand='1')
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
