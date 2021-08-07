import subprocess
import settings as s

class CommandExecuter:
    
    def __init__(self):
        self.interpreter = '/bin/bash'
            
    def execute(self, command):
        subprocess.Popen(command, shell=True, executable=self.interpreter)

class Command:
    def __init__(self):
        self.cmd=""
    
    def add_command(self, c):
        self.cmd += f"{c}; "
    
    def get_command(self):
        return self.cmd
