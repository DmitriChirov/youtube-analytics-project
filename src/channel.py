import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str):
        """При инициализации создаются атрибуты с основной информацией о канале"""
        self.__channel_id = channel_id
        self.channel_summary_info = self.get_service().channels().list(id=self.__channel_id,
                                                                       part='snippet,statistics').execute()  # получить информацию о канале
        self.title = self.channel_summary_info['items'][0]['snippet']['title']
        self.description = self.channel_summary_info['items'][0]['snippet']['description']
        self.url_channel = 'https://www.youtube.com/channel/' + self.__channel_id
        self.subscribers_count = self.channel_summary_info['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel_summary_info['items'][0]['statistics']['videoCount']
        self.view_count = self.channel_summary_info['items'][0]['statistics']['viewCount']

    def __str__(self):
        """Выводит название и ссылку на канал по шаблону `<название_канала> (<ссылка_на_канал>)`"""
        return f"'{self.title} ({self.url_channel})'"

    def __add__(self, other):
        return int(self.subscribers_count) + int(other.subscribers_count)

    def __sub__(self, other):
        return int(self.subscribers_count) - int(other.subscribers_count)

    def __eq__(self, other):
        return int(self.subscribers_count) == int(other.subscribers_count)

    def __lt__(self, other):
        return int(self.subscribers_count) < int(other.subscribers_count)

    def __le__(self, other):
        return int(self.subscribers_count) <= int(other.subscribers_count)

    def __gt__(self, other):
        return int(self.subscribers_count) >= int(other.subscribers_count)

    def __ge__(self, other):
        return int(self.subscribers_count) >= int(other.subscribers_count)

    @classmethod
    def get_service(cls):
        """Возвращает специальный объект для работы с ютуб-API"""
        return build('youtube', 'v3', developerKey=os.environ['YT_API_KEY'])

    @property
    def channel_id(self) -> str:
        """Возвращает идентификатор канала"""
        return self.__channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале в json-подобном удобном формате с отступами"""
        print(json.dumps(self.channel_summary_info, indent=2, ensure_ascii=False))

    def to_json(self, filename):
        """Сохраняет в файл значения атрибутов экземпляра Channel"""
        data = self.__dict__
        del (data['channel_summary_info'])
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=2, ensure_ascii=False)
