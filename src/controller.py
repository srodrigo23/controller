from view.main_view import MainView
import settings as s
import time
from video_reader import VideoReader

class Controller:
    
    def __init__(self, num_cams):
        self.num_cams = num_cams
        self.view = None
        self.video_reader = VideoReader(s.empty_video, self.num_cams)
        self.video_reader.start()
        
    def get_frame(self, id_camera):
        return self.video_reader.get_frame_from_queue(id_camera)
    
    def get_list_videos(self):
        return s.videos
    
    def set_view(self, view):
        self.view = view
        
    def get_time(self):
        return time.strftime('%H:%M:%S')