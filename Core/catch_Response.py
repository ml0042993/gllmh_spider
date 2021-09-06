import requests
import static
# 得到输入网页的源代码
class Catch_Page:
	def __init__(self,base_url):
		self.base_url = base_url

	def base_Catch(self):
		try:
			self.process_html=requests.get(self.base_url,headers=static.HEARD,timeout=1000)
			return self.process_html#返回首页的html源代码
		except(ConnectionError):
			print("连接超时")
		except Exception as e:
			print("未知错误")
			print(e.args)
if __name__ == '__main__':
	fun = Catch_Page(static.BASE_URL)
	aaa = fun.base_Catch()
	print(aaa.text)