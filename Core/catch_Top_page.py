from Core.catch_Response import Catch_Page
from bs4 import BeautifulSoup
import static
class process_Html:
	def __init__(self,base_Url):
		self.url = base_Url
		self.source_html = Catch_Page(self.url).base_Catch()#初始化得到的网页源文件代码

	def catch_Top_page(self):
		print(self.source_html)

if __name__ == '__main__':
	fun = process_Html(static.BASE_URL)
	fun.catch_Top_page()