# coding: utf-8
'''
	策略模式
'''

import abc

class Strategy(abc.ABC):
	"""策略接口，定义策略对象的功能。"""
	@abc.abstractmethod
	def get_result(self):
		pass
		

class StrategyOne(Strategy):
	"""具体的策略对象 One，实现策略接口。"""
	def __init__(self, name):
		super(StrategyOne, self).__init__()
		self.name = name
		
	def get_result(self):
		print('Strategy One:', self.name)
		return self.name

class StrategyTwo(Strategy):
	"""具体的策略对象 Two，实现策略接口。"""
	def get_result(self):
		print('Strategy Tow running...')
		return '2'

class StrategyThree(Strategy):
	"""策略对象 Three"""
	def __init__(self, value):
		super(StrategyThree, self).__init__()
		self.value = value
		
	def get_result(self):
		print('Strategy Three\'s value:', self.value)
		self.value += 1
		return self.value
		

class Context(object):
	"""策略上下文对象，客户端通过该对象来调用策略的具体方法。"""
	def __init__(self, strategy):
		super(Context, self).__init__()
		self.strategy = strategy
		
	def invoke(self):
		return self.strategy.get_result()

if __name__ == '__main__':
	while True:
		arg = input('输入 One / Two / Three 来运行相应的策略，或输入其它退出:')
		if arg == 'One':
			context = Context(StrategyOne('jerry'))
			print(context.invoke())
		elif arg == 'Two':
			context = Context(StrategyTwo())
			print(context.invoke())
		elif arg == 'Three':
			context = Context(StrategyThree(3))
			print(context.invoke())
		else:
			break


class FactoryContext(object):
	"""策略与简单工厂结合，将客户端的分支选择合并到策略上下文，使客户端与具体的策略对象解耦。"""
	def __init__(self, selected):
		super(FactoryContext, self).__init__()
		if selected == 'One':
			self.strategy = StrategyOne('giggs')
		elif selected == 'Two':
			self.strategy = StrategyTwo()
		elif selected == 'Three':
			self.strategy = StrategyThree(0)

	def invoke(self):
		return self.strategy.get_result()

if __name__ == '__main__':
	print('=====================================')
	while True:
		arg = input('输入 One / Two / Three 来运行相应的策略，或输入其它退出:')
		if arg not in ['One', 'Two', 'Three']:
			break
		context = FactoryContext(arg)
		print(context.invoke())













