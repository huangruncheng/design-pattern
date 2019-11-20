'''
	代理模式
	1、远程代理：代理远程对象，让客户端感觉象是在使用本地对象一样方便。
	2、虚拟代理：代理中保存那些创建时需要很消耗资源的对象。
	3、安全代理：在代理中进行安全验证。
'''

import abc

class Request(abc.ABC):
	"""定义请求方法的接口类。"""
	@abc.abstractmethod
	def request_a(self):
		pass

	@abc.abstractmethod
	def request_b(self):
		pass


class RealObject(Request):
	"""真实操作对象，共同实现 Request 接口。"""
	def request_a(self):
		print('真实请求 a')

	def request_b(self):
		print('request real object b')


class Proxy(Request):
	'''代理对象，共同实现 Request 接口。'''
	real_object = None
	def request_a(self):
		if self.real_object == None:
			print('create real object.')
			self.real_object = RealObject()
		# 在代理中可作安全验证等。
		self.real_object.request_a()

	def request_b(self):
		if self.real_object == None:
			print('create real object.')
			self.real_object = RealObject()
		self.real_object.request_b()



if __name__ == '__main__':
	proxy = Proxy()
	proxy.request_a()		# 客户端直接使用代理即可，不需要知道真实对象。
	proxy.request_b()

























