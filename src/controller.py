from view.main_view import MainView
from settings import Settings
from video_reader import VideoReader

from launcher import launch_server
from launcher import launch_camera

import time
import os, signal

class Controller:
    
    def __init__(self):
        self.view = None # to control view
        self.settings = Settings()
        self.num_cams = self.settings.get_num_cams()
        self.video_reader = VideoReader(self.settings.get_empty_video(), self.num_cams)
        self.video_reader.start() # to change
        self.server_process = None
    
    def kill_server(self):
        """
        Method to kill server process turning off the server
        """
        if self.server_process:
            os.kill(self.server_process.pid + 1, signal.SIGTERM)
        
    
    def connect_to_server(self):
        if self.server_process:
            pass
        else:
            self.view.server_panel.show_error_message("Error connecting", 
                                                      "Imposible to connect to the server")
    
    def launch_camera_process(self, video_path):
        """
        Method to run a camera process and return process id to show in the screen
        """
        sys_path = self.settings.get_system_camera_path()
        videos_folder_path = self.settings.get_videos_path()
        
        self.camera_process = launch_camera(sys_path, 
                                            os.path.sep.join[videos_folder_path, video_path])
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
