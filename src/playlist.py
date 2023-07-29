import json
import os
from googleapiclient.discovery import build


class PlayList:
    """Создает экземпляры объектов с информацией о плейлисте Ютуб"""

    def __init__(self, playlist_id: str):
        self.__playlist_id: str = playlist_id
        self.youtube = self.get_service()
        self.pl_summary_info = self.youtube.playlistItems().list(playlistId=playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()
        self.pl_summary_info_1 = self.youtube.playlists().list(id=playlist_id, part='snippet,contentDetails', maxResults=50).execute()
        self.playlist_url = 'https://www.youtube.com/playlist?list=' + self.playlist_id
        self.pl_title = self.pl_summary_info_1.get('items')[0].get('snippet').get('title')

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

    def print_info_1(self) -> None:
        """Выводит в консоль информацию о видео-ролике в json-подобном удобном формате с отступами"""
        print(json.dumps(self.pl_summary_info_1, indent=2, ensure_ascii=False))

# pl_test = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
# pl_test.print_info()
# pl_test.print_info_1()
# print(pl_test.pl_title)

# https://www.youtube.com/playlist?list=PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw