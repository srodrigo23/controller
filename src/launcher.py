
import subprocess
from settings import Settings

def launch_camera(sys_path, video_path):
    cmd = ""
    cmd += f"source .venv/bin/activate; "
    cmd += f"python src/main.py CAM '{video_path}'"
    return subprocess.Popen(cmd, shell=False, executable='/bin/bash', start_new_session=True, cwd=sys_path)

def launch_server(sys_path):
    cmd = ""
    cmd += f"source .venv/bin/activate; "
    cmd += f"python src/main.py"
    return subprocess.Popen(cmd, 
                            # shell=True,
                            # stdout=subprocess.PIPE,
                            # stderr=subprocess.PIPE,
                            # executable='/bin/bash', 
                            # start_new_session=True, 
                            cwd=sys_path)

def kill_process(process):
    process.kill()

# s = Settings()
# sys_path, venv_path = s.get_system_camera_path()
# video_path = 0
# video_path1 = '/Users/sergiorodrigo/Documents/tesis/code/videos/video7.mp4' #pasto
# video_path2 = '/Users/sergiorodrigo/Documents/tesis/code/videos/video8.mp4' #estacionamiento
# sys_path= s.get_system_camera_path()
# sys_path = s.get_system_server_path()
# launch_camera(sys_path, video_path1)
# launch_camera(sys_path, video_path2)

# launch_server(sys_path)
