import urllib.request
#import urllib3
#import pytest
#from selenium import webdriver
def getlinks(url):
	file=format(urllib.request.urlopen(url).read())
	#http=urllib3.PoolManager()
	#file=format(http.request("GET",url).data)
	#driver=webdriver.Firefox()
	#print("OK")
	#driver.get(url)
	#page=driver.page_source
	videolist=set()
	b=0
	while(True):
		try:
			a=file.index("\"url\":\"/watch?v=",b+1)
			b=file.index("\"",a+15)
			videolist.add("www.youtube.com/watch?v" + file[a+15:b][0:12])
		except:
			break
	print(videolist)
	return (videolist)
