import os

class FileRetriever:
    DATA_RELATIVE_DIR_PATH = 'data/'
    
    def __init__(self, url) -> None:
        self.__url = url
