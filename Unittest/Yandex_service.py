import requests
from Yandex_token import ya_disk_token

token = ya_disk_token
url = 'https://cloud-api.yandex.net:443/v1/disk/resources'
headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth ' + token}


def create_folder(folder_name):
    params = {'path': folder_name}
    response = requests.put(url=url, headers=headers, params=params)
    return response.status_code


def get_folder_info(folder_name):
    params = {'path': folder_name}
    response = requests.get(url=url, headers=headers, params=params)
    if response.status_code == 200:
        res_dict = response.json()
        return res_dict['type']


def delete_folder(folder_name):
    params = {'path': folder_name}
    response = requests.delete(url=url, headers=headers, params=params)
    return response.status_code


if __name__ == '__main__':
    create_folder('TEST_FOLDER')
    print(get_folder_info('TEST_FOLDER'))
    # delete_folder('TEST_FOLDER')