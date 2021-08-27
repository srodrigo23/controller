import os
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

class Settings():

    def __init__(self):
        self.path_file = '../config.yaml'
        self.read_file()

    def read_file(self):
        with open(self.path_file, 'r') as content:
            self.data = load(content, Loader=Loader)

    def get_num_cams(self):
        return self.data['num_cams']
        
    def get_resolution(self):
        return (self.data['resolution'][0], self.data['resolution'][1])

    def get_host_address(self):
        return self.data['host_address']

    def get_port(self):
        return self.data['port']
        
    def get_sys_path(self):
        return os.path.abspath(self.data['relative_path'])
    
    def get_videos_path(self):
        return os.path.sep.join([self.get_sys_path(), self.data['videos_folder_name']])
    
    def get_system_path(self, sys_name):
        sys_path = self.get_sys_path()
        folder_name = self.data[f'{sys_name}_folder_name']

        src = self.data['src_folder_name']
        main = self.data['main_file']

        return os.path.sep.join([sys_path, folder_name, src, main]), os.path.sep.join([sys_path, folder_name] + self.data['path_venv'])
    
    def get_system_camera_path(self):
        return self.get_system_path('camera')

    def get_system_server_path(self):
        return self.get_system_path('server')
    
    def get_videos(self):
        return os.listdir(self.get_videos_path()), self.get_videos_path()
    
    def get_empty_video(self):
        return os.path.sep.join([self.get_videos_path(), self.data['default_video']])