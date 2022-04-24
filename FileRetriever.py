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
    
    # update can be called on instances of this class
    # therefore we establish a force_update parmeter
    # if True, the file will always be updated, regardless of it's age
    def update(self, force_update = False) -> None:
        needs_update = False if not force_update else True
        file_path, data_url = FileRetriever.get_file_path(), FileRetriever.get_data_file_url()

        # if it doesn't exist yet, it will be created
        if not os.path.isfile(file_path):
            needs_update = True
        else:
            if time.time() - int(os.stat(file_path).st_mtime) > 600:
                needs_update = True
                
        if needs_update:
            self.__archive()
            print('Updating file {} from URL {}'.format(file_path, data_url))
            try:
                request.urlretrieve(data_url, file_path)
            except Exception as e:
                print('\nURL {} not reachable anymore!\n({})'.format(data_url, e))
        else:
            print('Re-Using cached file {}'.format(file_path))

    def __archive(self) -> None:
        file_path = FileRetriever.get_file_path()
        archive_path = FileRetriever.get_file_to_archive_path()
        if os.path.isfile(file_path):
            os.rename(file_path, archive_path)
            print('Archived ' + file_path + ' at ' + archive_path)
    
    # add some static members
    def get_data_file_url() -> str:
        return FileRetriever.DATA_FILE_URL

    def get_file_path() -> str:
        return FileRetriever.DATA_RELATIVE_DIR_PATH + FileRetriever.DATA_FILE_NAME

    def get_file_to_archive_path() -> str:
        return FileRetriever.DATA_RELATIVE_ARCHIVE_DIR_PATH + datetime.now().strftime('%y%m%d_%H%M%S') + '_' + FileRetriever.DATA_FILE_NAME

if __name__ == '__main__':
    print('====== Initialize FileRetriever ======')
    fr = FileRetriever()
    print()

    print('====== try update() without force ======')
    fr.update()
    print()

    print('====== try update() with force ======')
    fr.update(True)
    print()
