# -*- coding=utf-8 -*-'''

from http import cookiejar
from os import remove
from urllib import request
from urllib.request import urlretrieve
import requests
from bs4 import BeautifulSoup

try:
    import http.cookiejar
except:
    import http.cookiejar as cookielib
try:
    from PIL import Image
except:
    pass
# request请求报头
headers = {'Host': 'movie.douban.com',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
           'Accept': 'text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8',
           'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
           'Accept-Encoding': 'gzip, deflate, br',
           'Referer':'https://accounts.douban.com/login?source=movie',
           'Content-Length':'191',
           'Cookie': 'll="108288"; bid=7GN-sAMHNMc; __utma=30149280.775723212.1512887158.1512899196.1516542779.3; __utmz=30149280.1512887158.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=30149280.17069; __utmb=30149280.21.10.1516542779; __utmc=30149280; push_noty_num=0; push_doumail_num=0; ap=1; ps=y; _vwo_uuid_v2=74A47A7111362CDDFFDE26BC884D5BB1|1d49983c0ffff335ad29e71ac48850e4; __utmt=1; as="https://movie.douban.com/"',
           'Upgrade-Insecure-Requests':'1'}
url = 'https://accounts.douban.com/login?source=movie'
# form 表单提交的数据
datas = {'source':'movie',
         'redir':'https://movie.douban.com/'}
# 尝试使用cookie信息
session = requests.session()
session.cookies = cookiejar.LWPCookieJar(filename="cookies")
try:
    session.cookies.load(ignore_discard=True)
except:
    print("Cookies未能加载")

# 获取验证码
def getcapthca():
    resp = request.urlopen(url)
    htmldata = resp.read().decode("utf-8")
    soup = BeautifulSoup(htmldata, "html.parser")
    # 利用bs4获得验证码图片地址,并且保存到本地
    img_src = soup.find('img', id='captcha_image')['src']
    urlretrieve(img_src, "captcha.jpg")
    try:
        im = Image.open('captcha.jpg')
        im.show()
        im.close()
    except:
        print('到本地目录打开captcha.jpg获取验证码')
    finally:
        capthca = input('输入验证码:')
        remove('captcha.jpg')
        captcha_id = soup.find(
            'input', {'type': 'hidden', 'name': 'captcha-id'}).get('value')
        return capthca, captcha_id

def loggin():
    datas['form_email'] = input('Please input your account:')
    datas['form_password'] = input('Please input your password:')
    captcha, captcha_id = getcapthca()
    # 增加表数据
    datas['captcha-solution'] = captcha
    datas['captcha-id'] = captcha_id
    login = requests.post(url, data=datas, headers=headers)
    page = login.text
    print(page)
    session.cookies.save()
    return page


if __name__ == '__main__':
    loggin()
