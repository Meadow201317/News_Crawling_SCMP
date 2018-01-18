#coding:utf-8
#crawl news in BloomBerg for the page with key word search

import requests
from bs4 import BeautifulSoup #导入bs4库
import re #导入正则库
import urllib3


def News_dig(website):
	
	web = requests.get(website)
	websoup = BeautifulSoup(web.text,'html.parser')
	
	title = websoup.find_all(class_="lede-text-only__hed") #新闻标题
	published_date = websoup.find_all(class_="lede-text-only__times") #发布时间
	abstract = websoup.find_all(class_="abstract__item-text") #新闻摘要
	main_body = websoup.find_all(class_="body-copy") #新闻主体
	
	
	for string in title:
		print (string.get_text())
		f.write(string.get_text())
	for string in published_date:
		print (string.get_text())
		f.write(string.get_text())
	for string in abstract:
		print (string.get_text())
		f.write(string.get_text())
	for string in main_body:
		print (string.get_text())
		f.write(string.get_text())
	f.close()
	
	return 


i=325
	
for j in range(2,3):
	pagesite = "https://www.bloomberg.com/search?query=aac+technology&endTime=2017-11-16T09:30:30.194Z&page="+str(j)
	newspage = requests.get(pagesite)#取搜索页面的html
	pagesoup = BeautifulSoup(newspage.text,'html.parser') #创建beautifulsoup对象	
	
	search_result = pagesoup.find_all(class_=re.compile("search-result-items"))#抓取主页中search-result-items的内容并保存成html文件
	#print(search_result)
	f = open('bloombergnews.html','w',encoding='utf-8')
	f.writelines(str(search_result))
	f.close()
	
	bloombergnews = BeautifulSoup(open("bloombergnews.html",encoding='UTF-8'),'html.parser')
		

	for news_href in bloombergnews.find_all(href=re.compile("https://www.bloomberg.com/news/articles/")):
		filename = "bb-cp-0"+str(i)+".txt"
		f = open(filename,'w',encoding='utf-8')
		link = 'link: '+ news_href.get('href')
		print (link)
		print (j)
		f.write(link)
		News_dig(news_href.get('href'))
		i = i+1
		print (i)
		
	#print (link.get('href'))
#News_dig(website="https://www.bloomberg.com/news/articles/2012-12-12/iphone-speaker-supplier-s-margin-beats-apple-chart-of-the-day");
	

