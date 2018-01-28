# -*- coding=utf-8 -*-'''
# 豆瓣正在上映电影以及影评
from urllib import request
from bs4 import BeautifulSoup
import re
import time
import jieba    #分词包
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy
import spider.login
def get_movie_list(page):
    URL = "https://movie.douban.com/cinema/nowplaying/beijing/"

    resp = request.urlopen(URL)
    htmldata = resp.read().decode("utf-8")
    soup = BeautifulSoup(htmldata, "html.parser")
    nowplaying = soup.find_all("div", id="nowplaying")
    movieList = nowplaying[0].find_all('li', class_='list-item')
    listItem = []
    for item in movieList:
        nowplaying_dict = {'id': item['id'], 'data-title': item['data-title'], 'data-score': item['data-score'],
                           'data-actors': item['data-actors']}
        # print(item['id'],item['data-title'],item['data-score'])
        movieharf = item.find_all('a', class_="ticket-btn")
        # for href in movieharf:
        nowplaying_dict['href'] = movieharf[0]['href']
        listItem.append(nowplaying_dict)
    print(listItem[0]['id'])
    return listItem


def get_movie_commnts(movie_list_id, start):
    comments_url = 'https://movie.douban.com/subject/' + movie_list_id + '/comments?start=' + str(
        start) + '&limit=20'
    resp_comments = request.urlopen(comments_url)
    comments_data = resp_comments.read().decode("utf-8")
    comments_soup = BeautifulSoup(comments_data, "html.parser")
    comments = comments_soup.find_all("div", id="comments")
    commentsList = comments[0].find_all('div', class_='comment-item')
    count = comments_soup.find('li', class_='is-active')
    count_str = count.find('span').get_text()
    num = re.findall(r'[^()]+', count_str)[1]
    commentsItem = []
    for comments_item in commentsList:
        comments_dict = {}
        # comments_dict['comments']=
        comments_all = comments_item.find_all('p', class_="")[0].get_text()
        commentsItem.append(comments_all)
    return commentsItem


if __name__ == "__main__":
    # page = spider.login.loggin()
    page =None
    movie_list = get_movie_list(page)
    name =[]
    for l in movie_list:
        name = l['id']
        content = []
        for i in range(0, 10):
            start = i * 20
            content.append(get_movie_commnts(l['id'], start))
        # fh = open(l['data-title']+".txt", 'w', encoding='utf8')
        str_value = ''
        cleaned_comments =''
        for s in range(len(content)):
            str_value = str_value + (str(content[s])).strip()
            pattern = re.compile(r'[\u4e00-\u9fa5]+')
            filterdata = re.findall(pattern, str_value)
            cleaned_comments =cleaned_comments+ ''.join(filterdata)
            # fh.write(cleaned_comments)
        time.sleep(10)
        # fh.close()
        # print(cleaned_comments)
        # 去掉停用词
        segment = jieba._lcut(cleaned_comments)
        word_count = pd.DataFrame({'segment':segment})
        stop_words = pd.read_csv("stopwords.txt",index_col=False,quoting=3, sep="\t", names=['stopword'],encoding='utf-8')
        word_count = word_count[~word_count.segment.isin(stop_words.stopword)]
        # 统计词频
        words_stat = word_count.groupby(by=['segment'])['segment'].agg({"size"})
        words_stat = words_stat.reset_index().sort_values(by=["size"], ascending=False)
        word_count = word_count.groupby(['segment']).size()
        # print(word_count.sort_values(ascending=False))

        # 用词云进行显示
        wordcloud = WordCloud(font_path="simhei.ttf", background_color="white", max_font_size=80)  # 指定字体类型、字体大小和字体颜色
        word_frequence = {x[0]: x[1] for x in words_stat.head(1000).values}

        word_frequence_list = []
        for key in word_frequence:
             temp = (key, word_frequence[key])
             word_frequence_list.append(temp)

        wordcloud = wordcloud.fit_words(word_frequence_list)
        plt.imsave(l['id']+'img.jpg', wordcloud)
        plt.imshow(wordcloud, interpolation='bilinear')

