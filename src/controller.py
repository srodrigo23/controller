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
    
    def run_server(self):
        sys_path = self.settings.get_system_server_path()
        self.process_server = launch_server(sys_path)
        print(self.process_server.pid)
    
    def kill_server(self):
        # print(self.process_server.poll)
        # print(f'to kill {self.process_server.pid}')
        os.kill(self.process_server.pid + 1, signal.SIGTERM)
        # self.process_server.terminate()
        # self.process_server.kill()
        # print(self.process_server.poll)
        
    def launch_camera_process(self, video_path):
        sys_path = self.settings.get_system_camera_path()
        self.process_camera = launch_camera(sys_path, video_path)
        print(self.process_camera.pid)
    
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
