# -*- coding=utf-8 -*-'''
# 豆瓣正在上映电影以及影评
from urllib import request
from bs4 import BeautifulSoup
import re

import jieba    #分词包
import pandas as pd


def get_movie_list():
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


def get_movie_commnts(movie_list, start):
    comments_url = 'https://movie.douban.com/subject/' + movie_list[0]['id'] + '/comments?start=' + str(
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
    movie_list = get_movie_list()
    content = []
    for i in range(0, 10):
        start = i * 20
        content.append(get_movie_commnts(movie_list, start))
    fh = open("comments.txt", 'w', encoding='utf8')
    str_value = ''
    cleaned_comments =''
    for s in range(len(content)):
        str_value = str_value + (str(content[s])).strip()
        pattern = re.compile(r'[\u4e00-\u9fa5]+')
        filterdata = re.findall(pattern, str_value)
        cleaned_comments =cleaned_comments+ ''.join(filterdata)
        fh.write(cleaned_comments)
    # print(cleaned_comments)
    # 进行文字统计
    s = jieba._lcut(cleaned_comments)
    word_count = pd.DataFrame({'s':s})
    stop_words = pd.read_csv("stopwords.txt",index_col=False,quoting=3, sep="\t", names=['stopword'],encoding='utf-8')
    word_count = word_count[~word_count.s.isin(stop_words.stopword)]
    word_count = word_count.groupby(['s']).size()
    print(word_count.sort_values(ascending=False))

    # 用词云进行显示

    # word_count.head()
    fh.close()
