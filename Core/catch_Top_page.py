from Core.catch_Response import Catch_Page
from pyquery import PyQuery as pq
from Config.Configuration import Site

class process_Html:
	def __init__(self,base_Url):
		self.url = base_Url
		self.source_html = Catch_Page(self.url).base_Catch()#初始化得到的网页源文件代码
		self.init_doc = pq(self.source_html.text)#将源文件初始化为PyQuery对象
		self.total_page = self.catch_Total_page()
	def catch_Total_page(self):#获取网页一共多少页
		self.total_page = self.init_doc('.pageinfo strong:first-child').text()
		#print(self.total_page.text(),type(self.total_page.text()))
		return self.total_page

	def joint_All_page(self):
		__total_page = int(self.total_page)
		with open("../TEMP/All_Url","w+",encoding="utf-8") as f:
			for i in range(__total_page,0,-1):
				result = Site.ORIGIN_URL.value.format(i)
				f.write(result + "\n")


	def test_fun(self):
		aaa = Site.ORIGIN_URL.value.format("1")
		print(aaa)
if __name__ == '__main__':
	fun = process_Html(Site.BASE_URL.value)
	# fun.catch_Total_page()
	Url_list= fun.joint_All_page()
	print(Url_list)
	# fun.test_fun()#