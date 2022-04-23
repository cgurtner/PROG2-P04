"""
__author__ = "Cyrill Gurtner"
__email__  = "gurtncyr@students.zhaw.ch"
"""
import os
import time
from datetime import datetime
from urllib import request

class FileRetriever:
    DATA_FILE_URL = 'https://dam-api.bfs.admin.ch/hub/api/dam/assets/20964153/master'
    DATA_FILE_NAME = 'erwerbsquote_nach_kanton.csv'
    DATA_RELATIVE_ARCHIVE_DIR_PATH = 'data/archive/'
    DATA_RELATIVE_DIR_PATH = 'data/'
    
    def __init__(self) -> None:
        self.update()
    
    def update(self) -> None:
        needs_update = False

        # if it doesn't exist yet, it will be created
        if not os.path.isfile(FileRetriever.get_file_path()):
            needs_update = True
        else:
            if time.time() - int(os.stat(FileRetriever.get_file_path()).st_mtime) > 600:
                needs_update = True
        if needs_update:
            print('Archiving old file if it exists')
            self.archive()
            print('Updating file {} from URL {}'.format(FileRetriever.get_file_path(), FileRetriever.get_data_file_url()))
            try:
                file = request.urlopen(FileRetriever.get_data_file_url())
            except Exception as e:
                print('URL {} not reachable anymore! ({})'.format(FileRetriever.get_data_file_url(), e))
            else:
                print('Processing file...')
                data = file.read().decode()
                to_file = open(FileRetriever.get_file_path(), 'w')
                to_file.write(data)
                to_file.close()
                print('Done.')
        else:
            print('Re-Using cached file {}'.format(FileRetriever.get_file_path()))

    def archive(self) -> None:
        if os.path.isfile(FileRetriever.get_file_path()):
            os.rename(FileRetriever.get_file_path(), FileRetriever.get_file_to_archive_path())
    
    # add some static members
    def get_data_file_url() -> str:
        return FileRetriever.DATA_FILE_URL

    def get_file_path() -> str:
        return FileRetriever.DATA_RELATIVE_DIR_PATH + FileRetriever.DATA_FILE_NAME

    def get_file_to_archive_path() -> str:
        return FileRetriever.DATA_RELATIVE_ARCHIVE_DIR_PATH + datetime.now().strftime('%y%m%d_%H%M%S') + '_' + FileRetriever.DATA_FILE_NAME

if __name__ == '__main__':
    fr = FileRetriever()
