import os

sys_path = os.path.abspath('../..')

videos_path = os.path.sep.join([sys_path, "videos"])
videos = os.listdir(videos_path)

empty_video = os.path.sep.join([videos_path, "empty_video.mp4"])

camera_sys_path = os.path.sep.join([sys_path, "camera","src", "main.py"])
camera_env_path = os.path.sep.join([sys_path, "camera", ".env", "bin", "activate"])

server_sys_path = os.path.sep.join([sys_path, "server", "src", "main.py"])
server_env_path = os.path.sep.join([sys_path, "server", ".env", "bin", "activate"])

video1 = os.path.sep.join([videos_path, videos[6]])