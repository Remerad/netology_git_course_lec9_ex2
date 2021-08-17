import requests
from pprint import pprint
API_BASE_URL = "https://cloud-api.yandex.net/v1/disk"


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        headers = {
            "Accept": "application/json",
            "Authorization": "OAuth " + token
        }
        params = {
            'path': file_path,
            'overwrite': True
        }
        response = requests.get(API_BASE_URL + "/resources/upload", params=params, headers=headers)
        pprint(response.json())
        upload_response = requests.put(url=response.json()['href'], data=open(file_path, 'rb'),
                                       params=params, headers=headers)
        return upload_response.status_code


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'titanic.csv'
    token = ''

    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    pprint(result)
