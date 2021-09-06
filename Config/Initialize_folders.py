import os
import Config.Config as Config
class initialize_Folders:
	def __init__(self):
		self.path = self.detection_Folder()
		self.creat_Folder(path)
	def detection_Folder(self):#检测当前绝对路径
		self.path = os.getcwd()
		return self.path

	def creat_Folder(self,path):
		try:
			if not os.path.exists(Config.TEMP_PATH):
				os.mkdir(path + "/TEMP")
			elif not os.path.exists(Config.DownLoad_Path):
				os.mkdir(path + "/DownLoad")
		except (FileExistsError):
			print("已创建文件夹")
			print("finish")

if __name__ == '__main__':
	path = self_Inspection().detection_Folder()
	self_Inspection().creat_Folder(path)
