import json
import os
from googleapiclient.discovery import build


class Video:
    """Класс для видео-ролика на сайте Youtube"""

    def __init__(self, video_id: str):
        """При инициализации создаются атрибуты с основной информацией о видео"""
        self.__video_id = video_id
        self.video_summary_info = self.get_service().videos().list(id=self.__video_id,
                                                                   part='snippet,statistics,contentDetails,topicDetails',
                                                                   ).execute()
        self.title: str = self.video_summary_info['items'][0]['snippet']['title']
        self.video_url = 'https://www.youtube.com/video/' + self.video_id
        self.view_count: int = int(self.video_summary_info['items'][0]['statistics']['viewCount'])
        self.like_count: int = int(self.video_summary_info['items'][0]['statistics']['likeCount'])
        self.comment_count: int = int(self.video_summary_info['items'][0]['statistics']['commentCount'])

    def __str__(self):
        """Выводит название видео-ролика"""
        return self.title

    @classmethod
    def get_service(cls):
        """Возвращает специальный объект для работы с ютуб-API"""
        return build('youtube', 'v3', developerKey=os.environ['YT_API_KEY'])

    @property
    def video_id(self) -> str:
        """Возвращает идентификатор видео-ролика"""
        return self.__video_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о видео-ролике в json-подобном удобном формате с отступами"""
        print(json.dumps(self.video_summary_info, indent=2, ensure_ascii=False))


class PLVideo(Video):
    """Класс для плейлиста видео-ролика на сайте Youtube"""

    def __init__(self, video_id: str, playlist_id: str):
        """При инициализации создаются атрибуты с основной информацией о видео и id плейлиста"""
        super().__init__(video_id)
        self.__video_id: str = video_id
        self.__playlist_id: str = playlist_id
        self.playlist_videos = self.get_service().playlistItems().list(playlistId=self.playlist_id,
                                                                       part='contentDetails',
                                                                       maxResults=50,
                                                                       ).execute()

    def __str__(self):
        """Выводит название видео"""
        return self.title

    @property
    def playlist_id(self) -> str:
        """Возвращает идентификатор плейлиста"""
        return self.__playlist_id
