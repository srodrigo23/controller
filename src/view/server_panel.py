import tkinter as tk
from tkinter.ttk import Button, Scrollbar
from tkinter import LabelFrame, Label, Listbox

class ServerPanel(LabelFrame):
    
    def __init__(self, parent, controller, text):
        tk.LabelFrame.__init__(self, parent, text=text, bg=controller.settings.get_bg_color())
        self.controller = controller
        # self.change_time()
        self.set_process_control()
        self.set_server_control()
        self.set_info_server()
        self.set_messages_loger()
        
        self.pid = 0
        self.turned_on = False
        
    def set_messages_loger(self):
        lblfrm_info = LabelFrame(self, text="Messages Log", bg=self.controller.settings.get_bg_color())
        lblfrm_info.pack(side='top', fill='both', expand=1, padx=5, pady=5)
        scroll_bar = Scrollbar(lblfrm_info, orient=tk.VERTICAL)
        self.messages_list = Listbox(lblfrm_info, yscrollcommand=scroll_bar.set)
        self.messages_list['selectforeground'] = "#ffffff"
        self.messages_list['selectbackground'] = "#00aa00"
        self.messages_list['selectborderwidth'] = 1
        self.messages_list.configure(exportselection=False)
        scroll_bar.config(command=self.messages_list.yview)
        scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
        self.messages_list.pack(expand=1, fill='both', padx=3)
        # frm_list.pack(side='top', fill='both', expand=1, padx=5, pady=5)
        
    def set_info_server(self):
        lblfrm_info = LabelFrame(self, text="Info", bg=self.controller.settings.get_bg_color())
        lblfrm_info.pack(side='top', fill='x', expand=0, padx=5, pady=5)
        lblfrm_info.columnconfigure(0, weight=1)
        lblfrm_info.columnconfigure(1, weight=1)
        lblfrm_info.columnconfigure(2, weight=1)
        
        lbl_node = Label(lblfrm_info, text='Nodes', font=("Helvetica", 15), bg=self.controller.settings.get_color_green())
        lbl_node.grid(row=0, column=0, sticky='ew', padx=2, pady=2)
        
        lbl_clients = Label(lblfrm_info, text='Clients', font=("Helvetica", 15), bg=self.controller.settings.get_color_green())
        lbl_clients.grid(row=1, column=0, sticky='ew', padx=2, pady=2)
        
        lbl_time = Label(lblfrm_info, text='Time', font=("Helvetica", 15), bg=self.controller.settings.get_color_green())
        lbl_time.grid(row=2, column=0, sticky='ew', padx=2, pady=2)
        
        self.lbl_node_info = Label(lblfrm_info, text='N/A', font=("Helvetica", 15), bg=self.controller.settings.get_color_yellow())
        self.lbl_node_info.grid(row=0, column=1, columnspan=2, sticky='ew', padx=2, pady=2)
        
        lbl_clients_info = Label(lblfrm_info, text='N/A', font=("Helvetica", 15), bg=self.controller.settings.get_color_yellow())
        lbl_clients_info.grid(row=1, column=1, columnspan=2, sticky='ew', padx=2, pady=2)
        
        lbl_clock = Label(lblfrm_info, text='N/A', font=("Helvetica", 15), bg=self.controller.settings.get_color_yellow())
        lbl_clock.grid(row=2, column=1, columnspan=2, sticky='ew', padx=2, pady=2)
        
    def set_server_control(self):
        lblfrm_launch = LabelFrame(self, text = "Control", bg=self.controller.settings.get_bg_color())
        lblfrm_launch.pack(side='top', fill='x', expand=0, padx=5, pady=5)
        
        # lblfrm_launch.rowconfigure(0, weight=1)
        lblfrm_launch.columnconfigure(0, weight=1)
        lblfrm_launch.columnconfigure(1, weight=2)

        self.btn_connect_server = Button(
            lblfrm_launch, text='Connect', command=lambda: self.controller.connect_to_server())
        self.btn_connect_server.grid(row=0, column=0, columnspan=2, sticky='ew', padx=2, pady=2)
        
        lblfrm_ip = LabelFrame(
            lblfrm_launch, text='IP', bg=self.controller.settings.get_bg_color())
        lblfrm_ip.grid(row=1, column=0, sticky='ew', padx=2, pady=2)
        
        lbl_ip = Label(lblfrm_ip, font=("Helvetica", 18),
                       bg=self.controller.settings.get_bg_color())
        lbl_ip['text'] = self.controller.settings.get_host_address()
        lbl_ip.pack(expand=0, fill='x')
        
        lblfrm_port = LabelFrame(
            lblfrm_launch, text='PORT', bg=self.controller.settings.get_bg_color())
        lblfrm_port.grid(row=1, column=1, sticky='ew', padx=2, pady=2)

        lbl_port = Label(lblfrm_port, font=("Helvetica", 18),bg=self.controller.settings.get_bg_color())
        lbl_port['text'] = self.controller.settings.get_port()
        lbl_port.pack(expand=0, fill='x')    
       
    def set_process_control(self):
        lblfrm_launch = LabelFrame(self, bg=self.controller.settings.get_bg_color())
        lblfrm_launch.pack(side='top', fill='x', expand=0, padx=5, pady=5)
        self.switch_server = Button(lblfrm_launch, text='Launch', command=self.action)
        self.switch_server.pack(side='left', expand=1, fill='x')
        lblfrm_pid = LabelFrame(lblfrm_launch, text='PID',
                                bg=self.controller.settings.get_bg_color())
        lblfrm_pid.pack(side='top', fill='x', expand=0)        
        self.lbl_pid = Label(lblfrm_pid, text='0000', bg=self.controller.settings.get_bg_color(), 
                        font=("Helvetica", 18), fg="Red")
        self.lbl_pid.pack(side='left', fill='x')
        
    def action(self):
        """
        Method to change status an action of turn on server, without bussines logic
        """
        if not self.turned_on:
            self.pid = self.controller.launch_server_process()
            if self.pid:
                self.turned_on = True
                self.switch_server.configure(text="kill")
                self.change_pid_server(self.pid)
        else:
            self.controller.kill_process(self.pid)
            self.turned_on = False
            self.switch_server.configure(text="Launch")
            self.change_pid_server('0000')
            
    
    def change_pid_server(self, pid):
        """
        Change the server process id on the screen
        """
        self.lbl_pid['text'] = pid
    
    def change_time(self):
        self.clock_label.config(text=self.controller.get_time())
        self.clock_label.after(1000, self.change_time)
    
    def set_time(self):
        self.clock_label.config(text=self.get_time())

    def show_error_message(self, title, message):
        tk.messagebox.showerror(title=title, message=message)
