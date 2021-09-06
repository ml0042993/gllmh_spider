from .catch_Response import Catch_Page
from bs4 import BeautifulSoup

class process_Html:
	def __init__(self):
		self.source_html = Catch_Page.base_Catch
		print(self.source_html)

if __name__ == '__main__':
	fun = process_Html()