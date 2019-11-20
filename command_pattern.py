# coding: utf-8
'''
	命令模式：	将命令接收者的命令操作封装成一个个命令对象，并且定义一个命令调用者对象对命令进行管理和记录。
				客户端通过创建命令对象，并传递给调用者，由调用者来管理、调用或拒绝客户端的命令。
'''

import abc


class Command(abc.ABC):
	"""命令对象接口，定义命令的参数、调用方法接口等。"""
	def __init__(self, name, **command_args):
		super(Command, self).__init__()
		self.name = name
		self.command_args = command_args
		self.receiver = None

	def set_receiver(self, receiver):
		self.receiver = receiver

	def excute(self):
		pass


class Command_1(Command):
	"""docstring for Command_1"""
	def excute(self):
		if self.receiver == None:
			print('未设置命令接收者，无法运行该命令。')
			return
		self.receiver.excute_command_1(self)

class Command_2(Command):
	"""docstring for Command_2"""
	def excute(self):
		if self.receiver == None:
			print('未设置命令接收者，无法运行该命令。')
			return
		self.receiver.excute_command_2(self)

class Command_3(Command):
	"""docstring for Command_3"""
	def excute(self):
		if self.receiver == None:
			print('未设置命令接收者，无法运行该命令。')
			return
		self.receiver.excute_command_3(self)


class Invoker(object):
	"""调用者，管理命令和记录日志，并可按条件拒绝命令。"""
	def __init__(self, max_mutton, max_chicken, max_eggplant):
		super(Invoker, self).__init__()
		self.max_mutton = max_mutton
		self.max_chicken = max_chicken
		self.max_eggplant = max_eggplant
		self.commands = []

	def add_command(self, command):
		if type(command) == Command_1:
			if self.max_mutton <= 0:
				print('羊肉串烤完了，取消命令。')
				return
			self.commands.append(command)
			self.max_mutton -= 1
		elif type(command) == Command_2:
			if self.max_chicken <= 0:
				print('鸡翅烤完了，换一个？')
				return
			self.commands.append(command)
			self.max_chicken -= 1
		elif type(command) == Command_3:
			if self.max_eggplant <= 0:
				print('茄子没有了，烤点肉吧。')
				return
			self.commands.append(command)
			self.max_eggplant -= 1

	def show_commands(self):
		for command in self.commands:
			print(command.name, command.command_args)

	def invoke(self):
		receiver = Receiver()
		for command in self.commands:
			command.set_receiver(receiver)		# 由 调用者 来设置 接收者，则 客户端 只需创建命令，不需要关联 接收者，使 接收者 与 客户端 解耦
			command.excute()
		self.commands = []


class Receiver(object):
	"""命令接收者，负责具体执行命令。"""
	def excute_command_1(self, command):
		print('Command 1 烤羊肉串:', command.command_args)

	def excute_command_2(self, command):
		print('Command 2 烤鸡翅:', command.command_args)
		
	def excute_command_3(self, command):
		print('Command 3 烤茄子:', command.command_args)



if __name__ == '__main__':
	invoker = Invoker(2, 2, 1)
	command1 = Command_1('羊肉串1', q1='加辣', q2='放孜然')
	invoker.add_command(command1)
	command2 = Command_1('羊肉串2', q1='放葱')
	invoker.add_command(command2)
	command3 = Command_2('鸡翅1', q1='加蜜糖')
	invoker.add_command(command3)
	command4 = Command_2('鸡翅2', q1='不要辣')
	invoker.add_command(command4)
	command5 = Command_3('茄子1', q1='多蒜', q2='多辣')
	invoker.add_command(command5)
	command6 = Command_3('茄子2')
	invoker.add_command(command6)

	invoker.invoke()










		
		
		