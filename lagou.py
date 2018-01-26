# -*- coding=utf-8 -*-'''
import requests
from bs4 import BeautifulSoup

class job():
    def __init__(self,company,companyid,salary,positionname):
        self.__company = company
        self.__companyid = companyid
        self.__salary = salary
        self.__positionname = positionname
    
    def getCompany(self):
        return  self.__company


URL= 'https://www.lagou.com/zhaopin/Java/'
headers ={
    'Host':'www.lagou.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Connection':'keep-alive',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
}
info = requests.get(URL, headers=headers)
data = BeautifulSoup(info.text,"html.parser")
jobinfo = data.findAll('ul',{'class':'item_con_list'})
companydata = jobinfo[1].find_all('li',class_='con_list_item default_list')
jobList =[]
for da in companydata:
    job1 = job(da.get('data-company'),da.get('data-companyid'),da.get('data-salary'),da.get('data-positionname'))
    print(job1.getCompany())
    jobList.append(job1)
print(jobList)  
