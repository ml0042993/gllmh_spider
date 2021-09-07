from Core.catch_Response import Catch_Page
class catch_Second_page():
	def __init__(self):
		pass

	def read_All_url(self):
		url_path = "../TEMP/All_Url"
		with open(url_path,"r",encoding="utf-8") as f:
			mess = f.readlines()
			for i in mess:
				result = Catch_Page(i).base_Catch()


if __name__ == '__main__':
	fun = catch_Second_page()
	fun.read_All_url()