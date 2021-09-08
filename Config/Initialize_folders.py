import os
from Config.Config import Site
class initialize_Folders:
	def __init__(self):
		self.path = self.detection_Folder()
		self.creat_Folder(self.path)

	def detection_Folder(self):#检测当前绝对路径
		path = os.path.abspath(os.path.dirname(os.getcwd()))
		return path

	def creat_Folder(self,path):
		try:
			TEMP_path = path + Site.TEMP_PATH.value
			DownLoad_Path = path + Site.DownLoad_Path.value
			if not os.path.exists(TEMP_path):
				os.mkdir(TEMP_path)
				# os.mknod(TEMP_path + "/All_url.txt")
			if not os.path.exists(DownLoad_Path):
				os.mkdir(DownLoad_Path)
		except (FileExistsError):
			print("已创建文件夹")
			print("finish")

		# except Exception as e:
		# 	print(e.args)
if __name__ == '__main__':
	path = initialize_Folders().detection_Folder()


