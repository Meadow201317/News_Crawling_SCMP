#coding:utf-8
#crawl news in SCMP for the page with key word search

import requests
from bs4 import BeautifulSoup #导入bs4库
import re #导入正则库

#response = requests.get("http://www.scmp.com/content/search/AAC?f[0]=ds_created%3A%5B2013-01-01T00%3A00%3A00Z%20TO%202016-01-31T23%3A59%3A59Z%5D")
#soup = BeautifulSoup(response.text,'html.parser') #创建beautifulsoup对象

def News_dig(website):
	
	response = requests.get(website)
	soup = BeautifulSoup(response.text,'html.parser') #创建beautifulsoup对象
	
	title = soup.find_all(class_="title") #新闻标题
	published_date = soup.find_all(class_="node-published") #发布时间
	updated_date = soup.find_all(class_="node-updated") #更新时间
	main_body = soup.find_all(class_="panel-pane pane-entity-field pane-node-body pane-first pos-0")[-1] #新闻主体
	#f = open('sc-cp-0104.txt','w',encoding='utf-8')
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
	
i = 381

for j in range(86,150):
	
	pagesite = "http://www.scmp.com/content/search/iphone?page="+str(j)+"&f[0]=ds_created%3A%5B2011-02-01T00%3A00%3A00Z%20TO%202015-02-28T23%3A59%3A59Z%5D"
	newspage = requests.get(pagesite)#取搜索页面的html

	pagesoup = BeautifulSoup(newspage.text,'html.parser') #创建beautifulsoup对象	

	search_result = pagesoup.find_all(class_=re.compile("search-result article"))#抓取主页中search-result article split的内容并保存成html文件
	#print(search_result)
	f = open('scmpnews.html','w',encoding='utf-8')
	f.writelines(str(search_result))
	f.close()

	scmpnews = BeautifulSoup(open("scmpnews.html",encoding='UTF-8'),'html.parser')

	
	for news_href in scmpnews.find_all(href=re.compile("/news")):
		scmpnews_href = 'http://www.scmp.com' + news_href.get('href')
		#print (scmpnews_href)
		#print (type(news_href))
		filename = "sc-cp-0"+str(i)+".txt"
		f = open(filename,'w',encoding='utf-8')
		link = 'link: '+ scmpnews_href
		print (link)
		print (j)
		f.write(link)
		News_dig(scmpnews_href)
		i = i+1
		print (i)
	

	
	
#News_dig(website="http://www.scmp.com/tech/article/2059344/oppo-and-vivo-are-samsung-out-2017-china");
	

