from Core.catch_Response import Catch_Page
from pyquery import PyQuery as pq
import static


class process_Html:
	def __init__(self,base_Url):
		self.url = base_Url
		self.source_html = Catch_Page(self.url).base_Catch()#初始化得到的网页源文件代码
		self.init_doc = pq(self.source_html.text)#将源文件初始化为PyQuery对象

	def catch_Total_page(self):#获取网页一共多少页
		total_page = self.init_doc('.pageinfo strong:first-child')
		#print(total_page.text())
		return total_page

if __name__ == '__main__':
	fun = process_Html(static.BASE_URL)
	fun.catch_Total_page()