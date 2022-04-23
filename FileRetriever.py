import os
import time
from datetime import datetime
from urllib.request import urlretrieve

class FileRetriever:
    DATA_FILE_URL = 'https://dam-api.bfs.admin.ch/hub/api/dam/assets/20964153/master'
    DATA_FILE_NAME = 'erwerbsquote_nach_kanton.csv'
    DATA_RELATIVE_ARCHIVE_DIR_PATH = 'data/archive/'
    DATA_RELATIVE_DIR_PATH = 'data/'
    
    def __init__(self) -> None:
        self.update()
    
    def update(self) -> None:
        path = FileRetriever.DATA_RELATIVE_DIR_PATH + FileRetriever.DATA_FILE_NAME
        needs_update = False

        # if it doesn't exist yet, it will be created
        if not os.path.isfile(path):
            needs_update = True
        else:
            if time.time() - int(os.stat(path).st_mtime) > 6:
                needs_update = True

        if needs_update:
            print('Archiving old file if it exists')
            self.archive()

            print('Updating file {} from URL {}'.format(path, FileRetriever.DATA_FILE_URL))
            urlretrieve(FileRetriever.DATA_FILE_URL, path)
        else:
            print('Re-Using cached file {}'.format(path))

    def archive(self) -> None:
        path = FileRetriever.DATA_RELATIVE_DIR_PATH + FileRetriever.DATA_FILE_NAME
        archived_path = FileRetriever.DATA_RELATIVE_ARCHIVE_DIR_PATH + datetime.now().strftime('%y%m%d_%H%M%S') + '_' + FileRetriever.DATA_FILE_NAME

        if os.path.isfile(path):
            os.rename(path, archived_path)


if __name__ == '__main__':
    fr = FileRetriever()
