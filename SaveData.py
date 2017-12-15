# -*- coding=utf-8 -*-'''

import mysql.connector


class Data:
    def __init__(self, title, url, user):
        self.__title = title
        self.__url = url
        self.__user = user

    def get_title(self):
        return self.__title

    def get_url(self):
        return self.__url

    def get_user(self):
        return self.__user


class ConnectSql:
    def insert(self, list):
        con = mysql.connector.connect(user='**', password='***', database='test', charset="utf8")
        cus = con.cursor()
        for l in list:
            print(l.get_title(), l.get_url(), l.get_user())
            cus.execute('insert into  user(name,url,username) values(%s,%s,%s)',
                        (l.get_title(), l.get_url(), l.get_user()))
            con.commit()
        cus.close()
        con.close()
