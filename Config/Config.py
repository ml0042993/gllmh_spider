from enum import Enum#将常量变为枚举型
class Site(Enum):#x枚举需要通过.value取值
	SITE_URL = "http://www.gllmh.com"
	BASE_URL = "http://www.gllmh.com/ymgj/list_1.html"
	ORIGIN_URL = "http://www.gllmh.com/ymgj/list_{}.html"
	TEMP_PATH = "/TEMP"
	DownLoad_Path = "/DownLoad"
	HEARD = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
	}

if __name__ == '__main__':
	print(Site.SITE_URL.value + "1")
	print(type(Site.SITE_URL))