from Core.catch_Response import Catch_Page
from Config.Configuration import Site
import os
class catch_Third_page(Catch_Page):
	def __init__(self):
		pass
		# super().__init__(base_url=self.itmes_info)
		# self.base_Catch()
		# self.change_PyQuery()
		# self.__total_page = self.init_doc#将源文件初始化为PyQuery对象
		# print(self.__total_page)

	def read_All_url(self):
		url_path = "../TEMP/second_Url"
		with open(url_path,"r",encoding="utf-8") as f:
			# itmes = f.readlines()
			tap = 1
			# self.mess = f.readlines(1)[0].replace('\n','')
			for itme in f.readlines():
				print(itme)
				print('开始第{}话'.format(str(tap)))
				# self.itmes_info = itme.replace("\n","")
				url = itme.replace("\n","")
				self.Catch_info(url)
				self.change_PyQuery()
				self.__total_page = self.init_doc  # 将源文件初始化为PyQuery对象
				self.joint_All_page()
				print('结束第{}话'.format(str(tap)))
				tap+=1
			# self.itmes_info = "http://www.gllmh.com/ymgj/8060.html"
			# print(self.itmes_info)
			# super().__init__(base_url=self.itmes_info)
			# self.base_Catch()
			# self.change_PyQuery()
			# self.__total_page = self.init_doc  # 将源文件初始化为PyQuery对象
			# self.joint_All_page()


	def joint_All_page(self):
		file_name = self.__total_page('.listltitle h3').text().replace(" ","")
		path_name = Site.DownLoad_Path.value + '/' +file_name
		if not os.path.exists(path_name):
			os.mkdir(path_name)
		# print(path_name)
		rules_spider = ['section p img',".inner p img",".inner img"]
		circulation_tap = 1
		for rule_spider in rules_spider:

			imgs_DL=self.__total_page(rule_spider)
			print(bool(imgs_DL))
			if bool(imgs_DL):
				imgs_DL = self.__total_page(rule_spider).items()
				print("找到匹配")
				with open(path_name+'/{}'.format(file_name),'w',encoding="utf-8") as f:
					tap = 1
					for item in imgs_DL:

						item = item.attr("src")
						f.write(item + "\n")
						super().__init__(item)
						result = self.base_Catch()
						# print(result)
						try:
							with open(path_name+'/{}'.format(str(tap)+'.jpg'),'wb') as ff:
								ff.write(result.content)
						except (AttributeError):
							print("图片格式不匹配")
							continue
						tap += 1
				print("完成拉取")
				break
			else:
				print("第{}次匹配，未找到爬虫规则".format(circulation_tap))
				circulation_tap += 1
				print("第{}次匹配".format(circulation_tap))
				# print(item)
		# with open("../TEMP/second_Url", "a", encoding="utf-8") as f:
		# 	for item in items:
		# 		item = item.attr('href')#<class 'pyquery.pyquery.PyQuery'>
		# 		item = Site.SITE_URL.value + item
		# 		print(item)
		#
		# 		f.write(item + '\n')
if __name__ == '__main__':
	fun = catch_Third_page()
	fun.read_All_url()