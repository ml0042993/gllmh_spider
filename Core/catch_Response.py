import requests
import static
# 得到输入网页的源代码
class Catch_Page:
	def __init__(self):
		self.BASE_URL = static.BASE_URL
	@staticmethod
	def base_Catch(self):
		self.html_r=requests.get(self.BASE_URL,headers=static.HEARD)
		return self.html_r

if __name__ == '__main__':
	fun = Catch_Page()
	aaa = fun.base_Catch()
	print(aaa.text)