
from video_capture import VideoCapture
import settings as s

class Model:
    
    def __init__(self, video_source):
        self.video_source = video_source
        
    def get_frame(self):
        return self.video_source.get_frame()
    
    def get_list_videos(self):
        return s.videos        