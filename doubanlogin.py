# -*- coding=utf-8 -*-'''

from http import cookiejar
from os import remove
from urllib.request import urlretrieve
import SaveData
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
headers = {'Host': 'www.douban.com',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
           'Accept-Encoding': 'gzip, deflate, br',
           'Referer': 'https://www.douban.com/',
           'Upgrade-Insecure-Requests':'1'}
url = 'https://www.douban.com/accounts/login'
# form 表单提交的数据
datas = {'source': 'index_nav'}
# 尝试使用cookie信息
session = requests.session()
session.cookies = cookiejar.LWPCookieJar(filename="cookies")
try:
    session.cookies.load(ignore_discard=True)
except:
    print("Cookies未能加载")
    # cookies加载不成功，则输入账号密码信息

# 获取验证码
def getcapthca():
    url1 = "https://www.douban.com/"
    r = requests.post(url1, datas, headers)
    page = r.text
    # print(page)
    soup = BeautifulSoup(page, "html.parser")
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
        # print(captcha_id)
        return capthca, captcha_id


def isLogin():
    url = 'https://douban.com/'
    logincode = session.get(url, headers=headers, allow_redirects=False).status_code
    # print(logincode)
    if logincode == 200:

        return True
    else:
        return False


def loggin():
    datas['form_email'] = input('Please input your account:')
    datas['form_password'] = input('Please input your password:')
    captcha, captcha_id = getcapthca()
    # 增加表数据
    datas['captcha-solution'] = captcha
    datas['captcha-id'] = captcha_id
    login = requests.post(url, data=datas, headers=headers)
    page = login.text
    # print(page)
    soup = BeautifulSoup(page, "html.parser")
    result = soup.findAll('div', attrs={'class': 'title'})
    # 进入豆瓣登陆后页面，打印热门内容
    # print(result)
    #保存列表
    nameList = []
    for item in result:
        # print(item)
        print(item.find('a').get_text(),item.find('a').get('href'))
        title = item.find('a').get_text()
        urlpath = item.find('a').get('href')
        data = Data(title, urlpath, "匿名")
        nameList.append(data)
        # 保存 cookies 到文件，
        # 下次可以使用 cookie 直接登录，不需要输入账号和密码
    session.cookies.save()
    return nameList


if __name__ == '__main__':
    if isLogin():
        print("已经登录成功！")
    else:
        loggin()
        list = loggin()
        con = ConnectSql()
        con.insert(list)
