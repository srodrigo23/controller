from view.main_view import MainView
from settings import Settings
from video_reader import VideoReader

from launcher import launch_server
# from launcher import kill_process

import time
import os, signal

class Controller:
    
    def __init__(self):
        self.view = None # to control view
        self.settings = Settings()
        self.num_cams = self.settings.get_num_cams()
        
        self.pid_server = -1
        # self.process_server = None
        
        self.video_reader = VideoReader(
            self.settings.get_empty_video(),
            self.num_cams)
        
        self.video_reader.start() # to change
    
    def run_server(self):
        sys_path = self.settings.get_system_server_path()
        self.process_server = launch_server(sys_path)
    
    def kill_server(self):
        # print(self.process_server.poll)
        
        os.kill(self.process_server.pid, signal.SIGTERM)
        # self.process_server.terminate()
        # self.process_server.kill()
        # print(self.process_server.poll)
        
    
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
