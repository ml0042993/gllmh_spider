from Config.Initialize_folders import initialize_Folders

class self_Inspection(initialize_Folders):
	def __init__(self):
		super().__init__()

fun = self_Inspection()
print(fun.path)
print("aaa")