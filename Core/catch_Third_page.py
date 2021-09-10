from Core.catch_Response import Catch_Page
from Config.Configuration import Site
import os
class catch_Second_page(Catch_Page):
	def __init__(self):
		self.read_All_url()
		# super().__init__(base_url=self.itmes_info)
		# self.base_Catch()
		# self.change_PyQuery()
		# self.__total_page = self.init_doc#将源文件初始化为PyQuery对象
		# print(self.__total_page)

	def read_All_url(self):
		url_path = "../TEMP/second_Url"
		with open(url_path,"r",encoding="utf-8") as f:
			itmes = f.readlines()
			# self.mess = f.readlines(1)[0].replace('\n','')
			# for itme in itmes:
			# 	self.itmes_info = itme.replace("\n","")
			# 	super().__init__(base_url=self.itmes_info)
			# 	self.base_Catch()
			# 	self.change_PyQuery()
			# 	self.__total_page = self.init_doc  # 将源文件初始化为PyQuery对象
			# 	self.joint_All_page()

			self.itmes_info = "http://www.gllmh.com/ymgj/8060.html"
			print(self.itmes_info)
			super().__init__(base_url=self.itmes_info)
			self.base_Catch()
			self.change_PyQuery()
			self.__total_page = self.init_doc  # 将源文件初始化为PyQuery对象
			self.joint_All_page()


	def joint_All_page(self):
		file_name = self.__total_page('h3').text()
		path_name = Site.DownLoad_Path.value + '/' +file_name
		if not os.path.exists(path_name):
			os.mkdir(path_name)
		print(path_name)
		#
		# with open("../TEMP/second_Url", "a", encoding="utf-8") as f:
		# 	for item in items:
		# 		item = item.attr('href')#<class 'pyquery.pyquery.PyQuery'>
		# 		item = Site.SITE_URL.value + item
		# 		print(item)
		#
		# 		f.write(item + '\n')
if __name__ == '__main__':
	fun = catch_Second_page()
	fun.joint_All_page()