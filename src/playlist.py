import json
import os
from googleapiclient.discovery import build


class Playlist:
    """Создает экземпляры объектов с информацией о плейлисте Ютуб"""

    def __init__(self, playlist_id: str):
        self.__playlist_id: str = playlist_id
        self.pl_summary_info = self.get_service().playlistItems().list(playlistId=self.playlist_id,
                                                                       part='contentDetails',
                                                                       maxResults=50,
                                                                       ).execute()
        self.playlist_url = 'https://www.youtube.com/video/' + self.__playlist_id
        self.pl_title = None

    @classmethod
    def get_service(cls):
        """Возвращает специальный объект для работы с АПИ Ютуб"""
        return build('youtube', 'v3', developerKey=os.environ['YT_API_KEY'])

    @property
    def playlist_id(self) -> str:
        """Возвращает идентификатор плейлиста"""
        return self.__playlist_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о видео-ролике в json-подобном удобном формате с отступами"""
        print(json.dumps(self.pl_summary_info, indent=2, ensure_ascii=False))

# pl_test = Playlist()
