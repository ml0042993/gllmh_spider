import requests
import static
# 得到输入网页的源代码
class Catch_Page:
	def __init__(self,base_url):
		self.base_url = base_url

	def base_Catch(self):
		try:
			self.process_html=requests.get(self.base_url,headers=static.HEARD,timeout=10)

# encoding是从http中的header中的charset字段中提取的编码方式，若header中没有charset字段则默认为ISO-8859-1编码模式，则无法解析中文，这是乱码的原因。
# apparent_encoding会从网页的内容中分析网页编码的方式，所以apparent_encoding比encoding更加准确。当网页出现乱码时可以把apparent_encoding的编码格式赋值给encoding。

			self.process_html.encoding = self.process_html.apparent_encoding#解决乱码问题
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
	# print(aaa.content)