
import subprocess
from settings import Settings

def launch_camera(sys_path, video_path):
    cmd = ""
    cmd += f"source .venv/bin/activate; "
    cmd += f"python src/main.py cam '{video_path}'"
    return subprocess.Popen(cmd, shell=False, executable='/bin/bash', start_new_session=True, cwd=sys_path)

def launch_server(sys_path):
    cmd = ""
    cmd += f"source .venv/bin/activate; "
    cmd += f"python src/main.py"
    return subprocess.Popen(cmd, 
                            shell=True,
                            # stdout=subprocess.PIPE,
                            # stderr=subprocess.PIPE,
                            executable='/bin/bash', 
                            start_new_session=True, 
                            cwd=sys_path)