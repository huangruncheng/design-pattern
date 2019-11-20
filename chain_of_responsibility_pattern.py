# coding: utf-8
'''
	职责链模式：	使多个对象都有机会处理请求，从而避免请求的发送者和接收者之间的耦合关系。
				将这个对象连成一条链，并沿着这条链传递该请求，直到有一个最终完成处理。
'''

import abc


class IHandle(abc.ABC):
	"""处理请求的接口定义，由各级处理对象实现。"""
	def __init__(self, name):
		super(IHandle, self).__init__()
		self.name = name
	
	def set_header(self, header):
		self.header = header

	@abc.abstractmethod
	def handle(self, request):
		pass



class Request(object):
	"""请求对象，代表具体的请求。"""
	def __init__(self, name, typ, content, value):
		super(Request, self).__init__()
		self.name = name
		self.typ = typ
		self.content = content
		self.value = value
		
class TeamLeader(IHandle):
	"""组长角色，代表一个处理对象。"""
	def handle(self, request):
		if request.typ == '请假' and request.value <=3:
			print('{} 批准了 {} 请假 {} 天的申请。请假原因：{}'.format(self.name, request.name, request.value, request.content))
		else:
			if self.header:
				self.header.handle(request)


class Manager(IHandle):
	"""经理角色"""
	def handle(self, request):
		if request.typ == '请假':
			if request.value <= 5:
				print('{} 批准了 {} 请假 {} 天的申请。请假原因：{}'.format(self.name, request.name, request.value, request.content))
			else:
				if self.header:
					self.header.handle(request)
				else:
					print('{} 拒绝了 {} 请假 {} 天的申请。'.format(self.name, request.name, request.value))
		else:
			if self.header:
				self.header.handle(request)
		

class ChiefManager(IHandle):
	"""BOSS"""
	def handle(self, request):
		if request.typ == '加薪':
			if request.value <= 1000:
				print('{} 批准了 {} 加薪 {} 的申请。加薪原因：{}'.format(self.name, request.name, request.value, request.content))
			else:
				print('{} 拒绝了 {} 的加薪申请。'.format(self.name, request.name))
		elif request.typ == '请假':
			print('{} 批准了 {} 请假 {} 天的申请。请假原因：{}'.format(self.name, request.name, request.value, request.content))
		


if __name__ == '__main__':
	leader = TeamLeader('Timmy')
	manager = Manager('Mango')
	cm = ChiefManager('Candy')
	leader.set_header(manager)
	manager.set_header(cm)
	request1 = Request('jerry', '请假', '休年假', 3)
	leader.handle(request1)
	request2 = Request('jerry', '请假', '秋游', 8)
	leader.handle(request2)
	request3 = Request('tom', '加薪', '完成项目', 500)
	leader.handle(request3)
	request4 = Request('Micky', '加薪', '加班', 1500)
	leader.handle(request4)
	request5 = Request('giggs', '请假', '补休', 5)
	leader.handle(request5)










