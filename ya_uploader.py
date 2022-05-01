import requests


class YaUploader:
    def __init__(self, token):
        self.token = token

    def upload(self, file_path, file):
        try:
            href = self.get_upload_link(disk_file_path=file_path).get("href", "")
            if href == '':
                print('Загрузка завершилась ошибкой!')
                return
            response = requests.put(href, data=file, timeout=5)
            response.raise_for_status()
            if response.status_code != 201:
                print("Ошибка загрузки!")
        except:
            print('Загрузка завершилась ошибкой!')

    def _get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_upload_link(self, disk_file_path):
        try:
            upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
            headers = self._get_headers()
            params = {"path": disk_file_path, "overwrite": "true"}
            response = requests.get(upload_url, headers=headers, params=params, timeout=5)
            response.raise_for_status()
            result = response.json()
            result['status_code'] = response.status_code
            if response.status_code == 200:
                return result
            else:
                print('Не удалось получить ссылку для загрузки фото!')
                return result
        except:
            print('Не удалось получить ссылку для загрузки фото!')
            return {'status_code': response.status_code}


def get_link(disk_file_path='/test_hw/', token_path='tokens/ya_disk_token.txt'):
    try:
        with open(token_path) as f:
            ya_disk_token = f.read().strip()
    except:
        return 'token failure'
    uploader = YaUploader(ya_disk_token)
    return uploader.get_upload_link(disk_file_path)['status_code']


if __name__ == '__main__':
    pass


