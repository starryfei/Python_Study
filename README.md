## Python Spider

------------

 ### 豆瓣模拟登陆,获取首页热门内容--doubanlogin.py
- :fa-check:  post addresss: https://www.douban.com/accounts/login<br>
- :fa-check: capthca address: https://www.douban.com/
- :fa-check: 使用[tesseract-ocr](https://github.com/tesseract-ocr/ "tesseract-ocr")进行验证码识别,  需要下载安装并且设置环境变量**[wiki](https://github.com/tesseract-ocr/tesseract/wiki "wiki")**

------------

 ### 爬取豆瓣热门电影的短影评--MovieSpider.py readmoviedata.py
-  :fa-check: url https://movie.douban.com/cinema/nowplaying/beijing
-  :fa-check:使用*jieba wordcloud pandas matplotlib*等技术进行影评分析<br>
-  :fa-check: readmoviedata.py 是对保存的文件进行分析生成图片img<br>

------------

 ### 爬取拉钩Java的招聘信息lagou.py
- :fa-check: url:https://www.lagou.com/zhaopin/Java/
- :fa-check: 需要构造header,不能直接网页访问网页
- :fa-check: 抓取30页的数据需要休眠,
- :fa-check: url:https://www.lagou.com/zhaopin/Java/1/?filterOption=1

------------
