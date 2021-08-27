from view.main_view import MainView
from settings import Settings
from video_reader import VideoReader

import time

class Controller:
    
    def __init__(self):
        self.view = None # to control view
        self.settings = Settings()
        self.num_cams = self.settings.get_num_cams()
        self.video_reader = VideoReader(
            self.settings.get_empty_video(),
            self.num_cams)
        
        self.video_reader.start() # to change
        
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