from threading import Thread
from utils import resize
import sys, cv2, time

if sys.version_info >= (3, 0):
    from queue import Queue
else:
    from Queue import Queue

class VideoReader:
    
    def __init__(self, path_video, num):
        self.path = path_video
        self.stopped = False
        self.frame_queues = [] 
        self.num_queues = num
        self.setup_frame_queues()
    
    def setup_frame_queues(self):
        for i in range(self.num_queues):
            self.frame_queues.append(Queue(maxsize=32))
    
    def add_frame_to_all(self, frame):
        for i in range(self.num_queues):
            self.frame_queues[i].put(frame)

    def start(self):
        self.thread = Thread(target=self.read_frames, args=())
        self.thread.setDaemon(True)
        self.thread.start()
        
    def get_frame_from_queue(self, id_queue):
        return self.frame_queues[id_queue].get()
    
    def read_frames(self):
        while True:
            cap = cv2.VideoCapture(self.path)
            while True:
                ret, frame = cap.read()
                if ret:
                    frame = resize(frame, width=320)
                    self.add_frame_to_all(frame)
                else:
                    break
    
    def update(self):
        while self.source.isOpened():
            if self.stopped:
                return
            else:
                grabbed, frame = self.source.read()
                if grabbed:
                    self.frames_queue.put(frame)
                    
    # def __init__(self):
    #     self.video = cv2.VideoCapture(video_source)
    #     if not self.video.isOpened():
    #         raise ValueError("Unable to open video source", video_source)
        
    # Get video source width and height
    # self.width  = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
    # self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    #
    # def get_frame(self):
    #     if self.video.isOpened():
    #         ret, frame = self.video.read()
    #         frame = imutils.resize(frame, width=320)
    #         if ret:
    #             return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    #         else:
    #             return (ret, None)
    #     else:
    #         return None
    #   
    # def close_video_capture(self):
    #     if self.video.isOpened():
    #         self.video.release()