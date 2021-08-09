from command_executer import CommandExecuter
from command_executer import Command

import settings as s

class CameraLauncher:
    
    def __init__(self, video_name):
        self.video_name = video_name
        
        self.cmd = Command()
        self.cmd_exec = CommandExecuter()
        self.launch_camera()
        
    def launch_camera(self):
        cam_env_path = s.camera_env_path
        cam_sys_path = s.camera_sys_path
        
        self.cmd.add_command(f"source {cam_env_path}")
        self.cmd.add_command(f"python {cam_sys_path} -p {s.video1}")
        self.cmd_exec.execute(self.cmd.get_command())