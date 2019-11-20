'''
	状态模式：解决根据状态选择操作的分支条件问题。
'''

import abc, random

class Work(object):
	"""带状态的工作类，根据它不同的状态对它进行不同的操作。"""
	def __init__(self, name):
		super(Work, self).__init__()
		self.name = name
		self.state = StateA('default')

	def set_state(self, state):
		'''设置由哪个状态对象开始判断。'''
		self.state = state

	def change(self):
		self.state_value = random.randint(0, 5)



class BasicState(object):
	"""状态基类，各个具体状态继承这个类"""
	def __init__(self, name):
		super(BasicState, self).__init__()
		self.name = name
		
	@abc.abstractmethod
	def Work(self, work):
		'''各个状态对应操作的抽象方法，具体操作由子类实现'''

class StateA(BasicState):
	"""状态 A 的具体实现"""
	def Work(self, work):
		if 0 <= work.state_value < 2:
			print('StateA {} is working on {}...{}'.format(self.name, work.name, work.state_value))
		else:
			state = StateB('Jerry')
			state.Work(work)

class StateB(BasicState):
	"""状态 B 的具体实现"""
	def Work(self, work):
		if 2 <= work.state_value < 4:
			print('StateB {} is working on {}...{}'.format(self.name, work.name, work.state_value))
		else:
			state = StateC('Winnie')
			state.Work(work)

class StateC(BasicState):
	"""状态 C 的具体实现"""
	def Work(self, work):
		if 4 <= work.state_value < 6:
			print('StateC {} is working on {}...{}'.format(self.name, work.name, work.state_value))
		else:
			state = StateA('Tom')
			state.Work(work)


if __name__ == '__main__':
	for i in range(10):
		work = Work('worker0_0')
		work.change()
		StateA('Micky').Work(work)			# 客户端无需再做分支条件选择，可从第一个状态调用。如果状态连接成闭环，则可从任何一个状态开始调用。
		work.change()
		StateC('Puppy').Work(work)

	# StateA('Tom').Work(0)
	# StateA('Tom').Work(1)
	# StateA('Tom').Work(2)
	# StateA('Tom').Work(3)
	# StateA('Tom').Work(4)
	# StateA('Tom').Work(5)


# print('---------------- 等差数列求和 -----------------')
# def sum_n(An):
# 	return (An/2)*(1+An)		# 仅当 d = 1 时。
# print(sum_n(100), sum_n(50), sum_n(10), sum_n(5))


# def sum_n2(n, d):
# 	return n + n*(n - 1)*d/2	# 仅当 A1 = 1 时。
# print(sum_n2(100, 1), sum_n2(50, 1), sum_n2(10, 1), sum_n2(5, 1))
# print(sum_n2(100, 2), sum_n2(50, 2), sum_n2(10, 2), sum_n2(5, 2))
# print(sum_n2(50, 2), sum_n2(25, 2), sum_n2(5, 2), sum_n2(2, 2))
# print(sum_n2(34, 3), sum_n2(17, 3), sum_n2(4, 3), sum_n2(2, 3))


# # def sum_n3(an, d):
# # 	return (an*d/2)*(1+an)		# 公式错误，不存在这个公式。
# # print(sum_n3(100, 2), sum_n3(50, 2), sum_n3(10, 2), sum_n3(5, 2))

# def sum_n3(an, d):
# 	n = an // d
# 	print(1 + (n-1)*d)
# 	return sum_n2(n, d)
# print(sum_n3(100, 2), sum_n3(50, 2), sum_n3(10, 2), sum_n3(5, 2))  # 等于 print(sum_n2(50, 2), sum_n2(25, 2), sum_n2(5, 2), sum_n2(2, 2))

# def sum_n4(A1, n, d):
# 	return n*A1 + n*(n-1)*d//2
# print('按等差数列求和公式计算：', sum_n4(20, 30, 3))


# print(sum([1,3,5,7,9,   11,13,15,17,19]))


# an = 2.194 * 10**2 * pow(10, 3)
# print(sum_n(an))
# print(sum_n2(an, 1))













