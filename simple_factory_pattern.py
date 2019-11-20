''' 
	简单工厂模式：工厂类按客户端输入的选择来生成相应的算法类返回给客户端使用。
	适用：客户端中需要根据业务场景来选择不同的算法类。
'''

import abc

class Algorithm(abc.ABC):
	"""算法类接口，定义算法功能。"""
	@abc.abstractmethod
	def calculate(self, a, b):
		pass
	
class Add(Algorithm):
	"""算法类 1，计算和"""
	def calculate(self, a, b):
		return a + b

class Mul(Algorithm):
	"""算法类 2，计算积"""
	def calculate(self, a, b):
		return a * b

class SimpleFactory(object):
	"""简单工厂类，按客户端的输入生成具体的算法类。"""
	@classmethod
	def create_algorithm(cls, arg):
		if arg == '+':
			return Add()
		elif arg == '*':
			return Mul()


if __name__ == '__main__':
	algorithm = SimpleFactory.create_algorithm('+')
	print(algorithm.calculate(2, 5))
	algorithm = SimpleFactory.create_algorithm('*')
	print(algorithm.calculate(3, 7))

	# 反射
	cls = getattr(__import__('simple_factory_pattern'), 'SimpleFactory')
	print(cls)

