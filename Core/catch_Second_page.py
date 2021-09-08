from Core.catch_Response import Catch_Page
from Config.Config import Site

class catch_Second_page(Catch_Page):
	def __init__(self):
		self.read_All_url()
		super().__init__(base_url=self.mess)
		self.base_Catch()
		self.change_PyQuery()
		self.__total_page = self.init_doc#将源文件初始化为PyQuery对象
		# print(self.__total_page)

	def read_All_url(self):
		url_path = "../TEMP/All_Url"
		with open(url_path,"r",encoding="utf-8") as f:
			self.mess = f.readlines(1)[0].replace('\n','')
			# for i in mess:
			# print(self.mess)

	def joint_All_page(self):

		items = self.__total_page('.listl.list2 ul h3 a').items()
		for item in items:
			item = item.attr('href')#<class 'pyquery.pyquery.PyQuery'>
			item = Site.SITE_URL.value + item
			print(item)
			# print(type(item))

if __name__ == '__main__':
	fun = catch_Second_page()
	fun.joint_All_page()