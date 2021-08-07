
from view import View
from model import Model
from video_capture import VideoCapture

# to install opencv
#  pip install "opencv-python-headless<4.3"

class Controller:
    
    def __init__(self):
        self.video = VideoCapture()
        self.model = Model(self.video)
        self.view = View(self.model)