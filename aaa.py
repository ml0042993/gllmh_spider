class AAA:
	def __init__(self):
		self.Aaa()
		self.ccc = self.aaa
	def Aaa(self):
		self.aaa=1
	def Bbb(self):
		self.bbb=self.ccc

class BBB:
	def __init__(self,name):
		self.a=1
		self.b=2
		# self.asd()
		self.name = name
	def asd(self):
		self.d = 4

	@staticmethod
	def fff():
		e="aaaaa"
		return e
class CCC(BBB):
	def __init__(self):
		super().__init__(name="li")
		self.c=3
		self.asd()

if __name__ == '__main__':
	fun = CCC()
	print(fun.a)
	print(fun.b)
	print(fun.c)
	print(fun.d)
	print(fun.name)
	print(fun.fff())
	print(type(fun.fff()))

#
# def hi():
# 	return "hi yasoob!"
#
#
# def doSomethingBeforeHi(func):
# 	print("I am doing some boring work before executing hi()")
# 	print(func())
#
#
# doSomethingBeforeHi(hi)
#
#
# def a_new_decorator(a_func):
# 	def wrapTheFunction():
# 		print("在执行a_func()之前，我正在做一些无聊的工作")
#
# 		a_func()
#
# 		print("在执行a_func()之后，我正在做一些无聊的工作")
#
# 	return wrapTheFunction
#
#
# def a_function_requiring_decoration():
# 	print("我是需要一些装饰来去除我的臭味的功能")
#
#
# a_function_requiring_decoration()
# # outputs: "I am the function which needs some decoration to remove my foul smell"
#
# a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
# # now a_function_requiring_decoration is wrapped by wrapTheFunction()
#
# a_function_requiring_decoration()
# # outputs:I am doing some boring work before executing a_func()
# #        I am the function which needs some decoration to remove my foul smell
# #        I am doing some boring work after executing a_func()
# print(a_function_requiring_decoration.__name__)