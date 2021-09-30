from view.main_view import MainView
from settings import Settings
from video_reader import VideoReader

from launcher import launch_server
from launcher import launch_camera

import time
import os, signal
import socket 
class Controller:
    
    def __init__(self):
        self.view = None # to control view
        self.settings = Settings()
        self.num_cams = self.settings.get_num_cams()
        self.video_reader = VideoReader(self.settings.get_empty_video(), self.num_cams)
        self.video_reader.start() # to change
        self.server_process = None
        
        self.server_connected = False
    
    def kill_process(self, pid):
        """
        Method to kill server process turning off the server
        """
        os.kill(pid + 1, signal.SIGTERM)
        
    def connect_to_server(self):
        """
        Method to connect to server, connecting through sockets
        """
        if self.server_process:
            while not self.server_connected:
                try:
                    self.socket = socket.socket(
                        socket.AF_INET, socket.SOCK_STREAM)
                    self.socket.connect((self.settings.get_host_address(), self.settings.get_port()))
                    time.sleep(2.0)
                except socket.error as e:
                    print_log('e', f'Connection don\'t reached {str(e)}')
                else:
                    self.server_connected = True
                    print('connected')
                    # TODO listen messages
        else:
            self.view.server_panel.show_error_message("Error connecting", "Imposible to connect to the server")
    
    def launch_camera_process(self, video_name):
        """
        Method to run a camera process and return process id to show in the screen
        """
        sys_path = self.settings.get_system_camera_path()
        videos_folder_path = self.settings.get_videos_path()
        
        self.camera_process = launch_camera(sys_path, 
                                            os.path.join(videos_folder_path, video_name))
        return self.camera_process.pid
    
    def launch_server_process(self):
        """
        Method to run a server and return process id to show in the screen
        """
        sys_path = self.settings.get_system_server_path()
        self.server_process = launch_server(sys_path)
        return self.server_process.pid
    
    
    def get_frame(self, id_camera):
        return self.video_reader.get_frame_from_queue(id_camera)
    
    def get_videos(self):
        return self.settings.get_videos()
    
    def set_view(self, view):
        self.view = view
        
    def get_time(self):
        return time.strftime('%H:%M:%S')
    
    def get_num_cams(self):
        return self.num_cams
