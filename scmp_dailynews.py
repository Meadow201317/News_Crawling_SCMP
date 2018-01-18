#To crawl the scmp dailynews in the default page we open
#coding:utf-8

import requests
from bs4 import BeautifulSoup #导入bs4库
import re #导入正则库
import urllib3

def News_dig(website):
	
	response = requests.get(website)
	soup = BeautifulSoup(response.text,'html.parser') #创建beautifulsoup对象
	
	title = soup.find_all(class_="title") #新闻标题
	published_date = soup.find_all(class_="node-published") #发布时间
	updated_date = soup.find_all(class_="node-updated") #更新时间
	main_body = soup.find_all(class_="panel-pane pane-entity-field pane-node-body pane-first pos-0")[-1] #新闻主体
	
	for string in title:
		print (string.get_text())
		f.write(string.get_text())
	for string in published_date:
		print (string.get_text())
		f.write(string.get_text())
	for string in updated_date:
	#print (type(string))
		print (string.get_text())
		f.write(string.get_text())
	#print (main_body)
	for it in main_body:
		soupit = BeautifulSoup(str(it),"html.parser")
		res = soupit.get_text()
		print (res)
		f.write(res)
	f.close()
	return 

mainpage = requests.get("http://www.scmp.com/frontpage/hk") #获取scmp主页的内容
mainsoup = BeautifulSoup(mainpage.text,'html.parser') #创建beautifulsoup对象

content_wrapper = mainsoup.find_all(class_="content-wrapper")#抓取主页中content-wrapper的内容并保存成html文件
#print (content_wrapper)
f = open('scmpdailynews.html','w',encoding='utf-8')
f.writelines(str(content_wrapper))
f.close()

scmpdailynews = BeautifulSoup(open("scmpdailynews.html",encoding='UTF-8'))
for news_herf in scmpdailynews.find_all(href=re.compile("/news")):
	print ('http://www.scmp.com' + news_herf.get('href'))
	
	f = open('news_herf.txt','a',encoding='utf-8')
	f.write('http://www.scmp.com' + news_herf.get('href')+'\n')
	f.close()
	#i=1
	#website = 'http://www.scmp.com' + news_herf.get('href')
	#f = open('sc-'+str(i)+'.txt','w',encoding='utf-8')
	#i=i+1
	#News_dig(website);

