import cv2
import imutils
import time

# https://stackoverflow.com/questions/49084143/opencv-live-stream-video-over-socket-in-python-3/49095089

class VideoCapture:
    def __init__(self, video_source=0):
        # time.sleep(3)
        self.video = cv2.VideoCapture(video_source)
        if not self.video.isOpened():
            raise ValueError("Unable to open video source", video_source)
        
        # Get video source width and height
        # self.width  = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        # self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    
    def get_frame(self):
        if self.video.isOpened():
            ret, frame = self.video.read()
            frame = imutils.resize(frame, width=320)
            if ret:
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return None
        
    def close_video_capture(self):
        if self.video.isOpened():
            self.video.release()