from urllib.request import urlretrieve
from datetime import datetime

class FileRetriever:
    DATA_RELATIVE_DIR_PATH = 'data/'
    
    def __init__(self, url, name) -> None:
        self.__url = url
        self.__name = name
        self.update()
    
    def update(self) -> None:
        filename = datetime.now().strftime('%y%m%d_%H%M%S') + '_' + self.__name
        urlretrieve(self.__url, FileRetriever.DATA_RELATIVE_DIR_PATH + filename)

if __name__ == '__main__':
    url = 'https://dam-api.bfs.admin.ch/hub/api/dam/assets/20964153/master'
    fr = FileRetriever(url, 'erwerbsquote.csv')
