# -*- coding=utf-8 -*-'''
# 豆瓣正在上映电影以及影评
from urllib import request
from bs4 import BeautifulSoup



def get_movie_list():
    URL="https://movie.douban.com/cinema/nowplaying/beijing/"

    resp = request.urlopen(URL)
    htmldata = resp.read().decode("utf-8")
    # print(htmldata)
    #
    soup = BeautifulSoup(htmldata, "html.parser")
    nowplaying = soup.find_all("div",id="nowplaying")
    movieList = nowplaying[0].find_all('li',class_='list-item')
    listItem = []
    for item in movieList:
        nowplaying_dict ={}
        nowplaying_dict['id']=item['id']
        nowplaying_dict['data-title'] = item['data-title']
        nowplaying_dict['data-score'] = item['data-score']
        nowplaying_dict['data-actors'] = item['data-actors']
        # print(item['id'],item['data-title'],item['data-score'])
        movieharf=item.find_all('a',class_="ticket-btn")
        # for href in movieharf:
        nowplaying_dict['href'] = movieharf[0]['href']
        listItem.append(nowplaying_dict)
    print(listItem[0]['id'])
    return  listItem

def get_movie_commnts(movie_list):
    comments_url = 'https://movie.douban.com/subject/'+movie_list[0]['id']+'/comments?start=0'+'&limit=20'
    resp_comments = request.urlopen(comments_url)
    comments_data = resp_comments.read().decode("utf-8")
    # print(htmldata)
    comments_soup = BeautifulSoup(comments_data, "html.parser")
    comments = comments_soup.find_all("div",id="comments")
    commentsList = comments[0].find_all('div',class_='comment-item')
    commentsItem = []
    for comments_item in commentsList:
        comments_dict={}
        # comments_dict['comments']=
        print(comments_item.find_all('p', class_="")[0].get_text())
if __name__=="__main__":
    movie_list = get_movie_list()
    get_movie_commnts(movie_list)