import os
from datetime import datetime
from shutil import copyfile

class file_combine:
    def __init__(self,file_extension):
        self.file_extension = file_extension
        self._combined_file_data = []
        
        self._combined_filename = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        self._file_directory = self._combined_filename
        self._load()
    def _load(self):
        os.makedirs(self._file_directory)
        file_names = os.listdir()
        for file_name in file_names:
            if file_name.endswith(self.file_extension):
                try:
                    file_data = open(file_name)
                    for data in file_data:
                        self._combined_file_data.append(data)
                    copyfile(file_name,self._file_directory+"/"+file_name)
                except IndexError:
                    print("File format not valid ->"+file_name)
                    exit()
    def combine(self):
       combined_file = open(self._file_directory+"/"+self._combined_filename+"."+self.file_extension,"w+")
       for data in self._combined_file_data:
           combined_file.write(data)
    def get_combined_filename(self):
        return self._combined_filename

