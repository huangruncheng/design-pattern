'''
	工厂方法模式：对每一个算法类都对应一个工厂类，一个工厂只生成一个方法类。
	适用：对应不同的客户有不同的算法，但同一客户只使用一种算法类，且需要在多个地方生成算法类，可生成一个工厂保存在全局，供需要生成算法类的地方使用。
'''

import abc

class Algorithm(abc.ABC):
	"""算法类接口，定义算法功能。"""
	@abc.abstractmethod
	def dosth(self, *args):
		pass

class Factory(abc.ABC):
	"""工厂接口，定义工厂功能。"""
	def get_algorithm(self):
		pass



class AlgorithmForA(Algorithm):
	"""对应 A 客户的算法类。"""
	def dosth(self, *args):
		print('Algorithm for A.', args)

class FactoryForA(Factory):
	"""A 客户使用的工厂。"""
	def get_algorithm(self):
		return AlgorithmForA()
		


class AlgorithmForB(Algorithm):
	"""对应 B 客户的算法类。"""
	def dosth(self, *args):
		print('Algorithm for BBBBBB.', args)

class FactoryForB(Factory):
	"""B 客户使用的工厂。"""
	def get_algorithm(self):
		return AlgorithmForB()
		

if __name__ == '__main__':
	''' A 客户 '''
	factory = FactoryForA()					# 保存在全局变量，注意，只有这里不同。

	algorithm = factory.get_algorithm()		# 在多个地方使用工厂来创建算法类实例。
	algorithm.dosth()
	algorithm = factory.get_algorithm()		# 在多个地方使用工厂来创建算法类实例。
	algorithm.dosth(1,2,3)
	algorithm = factory.get_algorithm()		# 在多个地方使用工厂来创建算法类实例。
	algorithm.dosth('jerry', 25)


if __name__ == '__main__':
	''' B 客户 '''
	factory = FactoryForB()					# 保存在全局变量，注意，只有这里不同。

	algorithm = factory.get_algorithm()		# 在多个地方使用工厂来创建算法类实例。
	algorithm.dosth()
	algorithm = factory.get_algorithm()		# 在多个地方使用工厂来创建算法类实例。
	algorithm.dosth(1,2,3)
	algorithm = factory.get_algorithm()		# 在多个地方使用工厂来创建算法类实例。
	algorithm.dosth('jerry', 25)











