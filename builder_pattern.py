'''
	建造者模式（生成器模式）
	通过 指挥者 来确保 建造者 的所有步骤被执行，从而保证建造过程的完整。而不同的 建造者 可创建有不同表现 产品。
'''

import abc


class Product(object):
	"""产品类，代表要创建的对象。"""
	def __init__(self, name):
		super(Product, self).__init__()
		self.name = name
		self.members = []

	def add(self, member):
		self.members.append(member)

		
class Builder(abc.ABC):
	"""建造者接口，定义建造一个产品的所有操作。"""
	def __init__(self, name):
		self.product = Product(name)

	@abc.abstractmethod
	def stepA(self):
		pass
	
	@abc.abstractmethod
	def stepB(self):
		'''其中一个步骤'''

	@abc.abstractmethod
	def stepC(self):
		pass



class BuiderOne(Builder):
	"""具体的建造者 One"""
	def stepA(self):
		print('One stepA.')
		self.product.add('One A')
		
	def stepB(self):
		print('One stepB.')
		self.product.add('One B')

	def stepC(self):
		print('One stepC.')
		self.product.add('One C')



class BuilderTwo(Builder):
	"""具体的建造者 Two"""
	def stepA(self):
		print('Two step a.')
		self.product.add('Two a')

	def stepB(self):
		print('Two step b.')
		self.product.add('Two b')

	def stepC(self):
		print('Two step c.')
		self.product.add('Two c')
		


# 建造过程指挥者，保证建造过程的完整性。
class Director(object):
	"""指挥者"""
	def __init__(self, builder):
		super(Director, self).__init__()
		self.builder = builder

	def set_builder(self, builder):
		self.builder = builder

	def build(self):
		if self.builder:
			self.builder.stepA()
			self.builder.stepB()
			self.builder.stepC()
			return self.builder.product
		return None
		


if __name__ == '__main__':
	builder = BuiderOne('jerry')
	director = Director(builder)
	product = director.build()
	print(product.members)

	builder = BuilderTwo('giggs')
	director.set_builder(builder)
	product = director.build()
	print(product.members)













