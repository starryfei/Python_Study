# -*- coding=utf-8 -*-'''
import requests
from requests import RequestException
import os
from hashlib import md5


def download_image(url, title):
    print('正在下载', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            save_image(response.content, title)
        return None
    except RequestException:
        print('请求图片出错', url)
        return None
    except FileNotFoundError:
        print('保存到本地失败', url)
        return None


def save_image(content, title):
    image_dir = os.getcwd() + os.path.sep + 'images' + os.path.sep + title
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
    file_path = '{0}{1}{2}.{3}'.format(image_dir, os.path.sep, md5(content).hexdigest(), 'jpg')
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(content)
            f.close()


if __name__ == "__main__":
    url = ""
    title = ""
    download_image(url, title)
