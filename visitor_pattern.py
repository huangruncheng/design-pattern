'''
	访问者模式，通过双分派的方式实现在两种类型多种结合形式中的分支选择。
	优点：	1、将两种不同类型的组合解耦
			2、消除客户端的分支选择
'''
import abc

class BasicVisitor(abc.ABC):
	"""访问者基类，定义操作各种数据结构的抽象方法，访问者类型不固定，可随时扩展，定义新的访问者，不影响原有的访问者和客户端"""
	def __init__(self):
		super(BasicVisitor, self).__init__()

	@abc.abstractmethod
	def OperateElementA(self, element):
		'''操作数据结构 A'''

	@abc.abstractmethod
	def OperateElementB(self, element):
		'''操作数据结构 B'''


class VisitorA(BasicVisitor):
	"""访问者类，实现具体的操作方法"""
	def __init__(self):
		super(VisitorA, self).__init__()
		
	def OperateElementA(self, element):
		print('VisitorA is operating ElementA:', element.name)
		element.ActionOfA()

	def OperateElementB(self, element):
		print('VisitorA is operating ElementB:', element.name)
		element.ActionOfB()


class VisitorB(BasicVisitor):
	"""另一个访问者类，实现另一种操作数据的方法"""
	def __init__(self):
		super(VisitorB, self).__init__()

	def OperateElementA(self, element):
		element.ActionOfA()
		print('VisitorB doing sth. on ElementA:', element.name)

	def OperateElementB(self, element):
		element.ActionOfB()
		print('VisitorB doing sth. on ElementB:', element.name)

# ---------------------------------

class BasicElement(abc.ABC):
	"""数据结构基类，由子类定义具体数据，数据结构的类型个数固定，不能随意扩展，因为扩展则需修改所有的访问者类以增加相应的操作方法。"""
	def __init__(self, name):
		super(BasicElement, self).__init__()
		self.name = name

	@abc.abstractmethod
	def Accept(self, visitor):
		'''接受访问者访问的抽象方法，由各个子类具体实现'''


class ElementA(BasicElement):
	"""数据结构类 A"""
	def ActionOfA(self):					# 数据结构 A 自己的个性化操作
		print('I\'m ElementA, -_-!')

	def Accept(self, visitor):
		visitor.OperateElementA(self)		# 第二次分派，数据结构再向访问者传递自己，这里确定操作的 数据结构。

class ElementB(BasicElement):
	"""数据结构类 B"""
	def __init__(self, name):				# 这里的 __init__ 非必须，ElementA 就没定义。
		super(ElementB, self).__init__(name)
		self.name = name
		
	def ActionOfB(self):					# 数据结构 B 自己的个性化操作
		print('I\'m ElementB, o_0!')

	def Accept(self, visitor):
		visitor.OperateElementB(self)		# 第二次分派，数据结构再向访问者传递自己，这里确定操作的 数据结构。

# -----------------------------------

class ObjectStructure(object):
	"""对象结构类，维护数据结构列表，并提供高层方法给访问者访问数据结构"""
	def __init__(self):
		super(ObjectStructure, self).__init__()
		self.elements = []
		
	def Attach(self, element):
		self.elements.append(element)

	def Detach(self, element):
		self.elements.remove(element)

	def Visit(self, visitor):
		for element in self.elements:
			element.Accept(visitor)			# 第一次分派，将访问者传递给数据结构，这里确定操作的 访问者 。


# -------------------------------------

if __name__ == '__main__':
	objectStructure = ObjectStructure()
	objectStructure.Attach(ElementA('Dododo'))
	objectStructure.Attach(ElementB('Rerere'))

	objectStructure.Attach(ElementA('Mimimi'))
	objectStructure.Attach(ElementB('Fafafa'))

	objectStructure.Visit(VisitorA())
	objectStructure.Visit(VisitorB())

	print('=============================================')















