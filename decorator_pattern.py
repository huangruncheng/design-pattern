'''
	装饰器模式
	通过装饰器，在不修改原有对象的前提下，对原有对象的功能进行扩展。
'''

import abc

class Component(abc.ABC):
	"""对象操作的接口。"""
	@abc.abstractmethod
	def operate(self):
		pass


class OriObject(Component):
	"""原有对象"""
	def operate(self):
		print('Original Object')


class Decorator(Component):
	"""装饰器 基类"""
	def decorator(self, component):
		self.component = component

	def operate(self):
		if self.component:
			self.component.operate()


class DecoratorA(Decorator):
	"""装饰器 A"""
	def operate(self):
		super().operate()
		print('Decorator A operating...')
		

class DecoratorB(Decorator):
	"""装饰器 B"""
	def operate(self):
		super().operate()
		print('Decorator B ~~~')


class DecoratorC(Decorator):
	"""装饰器 C"""
	def operate(self):
		super().operate()
		print('Decorator C working...')


if __name__ == '__main__':
	ori = OriObject()

	decA = DecoratorA()
	decB = DecoratorB()
	decC = DecoratorC()

	decA.decorator(ori)
	decB.decorator(decA)
	decC.decorator(decB)

	decC.operate()

	print('----------------')

	decC.decorator(ori)
	decA.decorator(decC)

	decA.operate()
































		