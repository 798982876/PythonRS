# !/usr/bin/env python
#  -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib
import requests


# 加入Cookie和User-Agent信息
Cookieinfo = "tisSession=c44c80b9-1030-47e5-8f7b-73c849beeded; _ga=GA1.2.47882627.1556192252; _gid=GA1.2.323785396.1556192252"
User = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
headers = {'Cookie': Cookieinfo,
           'User-Agent': User
           }

rawurl = "https://ladsweb.modaps.eosdis.nasa.gov/archive/orders/501329453/"
req=urllib.request.Request(rawurl,headers={'Cookie': Cookieinfo,
           'User-Agent': User
           })
response= urllib.request.urlopen(req)
content=response.read().decode("ascii")#获得html页面

soup=BeautifulSoup(content,"html.parser")#解析页面

url_cand_html=soup.find_all(id='ftp-directory-list') #定位到存放url的div标签
list_urls=url_cand_html[0].find_all("a") #定位到a标签，其中存放着文件的url
urls=[]

for i in list_urls[1:145]:#共有文件数
    urls.append('https://ladsweb.modaps.eosdis.nasa.gov/archive/orders/501329453/'+i.get('href')) #取出链接

for i,url in enumerate(urls):
    print("This is file"+str(i+1)+" downloading! You still have "+str(145-i-1)+" files waiting for downloading!!")
    file_name = "E:/RSdata/"+url.split('/')[-1]
    r = requests.get(url, headers=headers)#获得数据
    with open(file_name, "wb") as code: 
        code.write(r.content)#写入文件


