'''
	抽象工厂模式：一个工厂生成一个系列的多个算法类。	算法类有多个系列，但每个系列实现相同的业务，只是每个系列有不同的实现方法。
	适用：例如不同的客户使用不同的数据库，则不同的数据库的对象组成不同系列的算法对象。这时每个客户使用不同的工厂，来生成对应不同数据库的一系列数据库对象。
'''

import abc

class User(abc.ABC):
	"""数据库对象 User 的接口，由不同的具体数据库对象来实现。"""
	def __init__(self, name, age, right):
		super(User, self).__init__()
		self.name = name
		self.age = age
		self.right = right

	def save(self):
		pass

class Department(abc.ABC):
	"""数据库对象 Department 的接口，由不同的具体数据库对象来实现。"""
	def __init__(self, name, prop):
		super(Department, self).__init__()
		self.name = name
		self.prop = prop
		
	def save(self):
		pass

class Factory(abc.ABC):
	"""工厂类接口，不同的数据库实现不同的工厂。"""
	@classmethod
	def create_user(cls, name, age, right):
		pass

	@classmethod
	def create_department(cls, name, prop):
		pass




# SqlServer
class SqlServerUser(User):
	"""Sql Server 的 User 类。"""
	def save(self):
		print('Sql Server save User object.', self.name, self.age, self.right)


class SqlServerDepartment(Department):
	"""Sql Server 的 Department 类。"""
	def save(self):
		print('Sql Server save Department object.', self.name, self.prop)


class SqlServerFactory(Factory):
	"""Sql Server 的工厂类。"""
	def create_user(self, name, age, right):
		return SqlServerUser(name, age, right)

	def create_department(self, name, prop):
		return SqlServerDepartment(name, prop)



# Oracle
class OracleUser(User):
	"""Oracle 的 User 类。"""
	def save(self):
		print('Oracle save User.', self.name)

class OracleDepartment(Department):
	"""Oracle 的 Department 类。"""
	def save(self):
		print('Oracle save Department', self.name)
		

class OracleFactory(Factory):
	"""Oracle 的工厂类。"""
	def create_user(self, name, age, right):
		return OracleUser(name, age, right)
		
	def create_department(self, name, prop):
		return OracleDepartment(name, prop)



if __name__ == '__main__':
	# Sql Server 客户
	factory = SqlServerFactory()
	user = factory.create_user('Tom', 25, 'admin')
	user.save()
	dept = factory.create_department('marketing', 'sell product')
	dept.save()


if __name__ == '__main__':
	# Oracle 客户
	print('------------------------------------')
	factory = OracleFactory()
	user = factory.create_user('Micky', 25, 'admin')
	user.save()
	dept = factory.create_department('hr', 'hr')
	dept.save()







"""-------------------用简单工厂结合反射来代替抽象工厂，可解决每增加一个数据库对象就要修改 Factory 接口和相应的具体工厂类的问题。------------------"""

class Employee(abc.ABC):
	"""新增 Employee 数据库对象。"""
	def __init__(self, name, level):
		super(Employee, self).__init__()
		self.name = name
		self.level = level

	@abc.abstractmethod
	def save(self):
		pass

class SqlServerEmployee(Employee):
	def save(self):
		print('Sql Server save Employee', self.name)

class OracleEmployee(Employee):
	def save(self):
		print('Oracle, save Employee', self.name)
		


class DataAccess(object):		# 无需实现接口，因为客户端只使用一个 DataAccess，不会按不同的数据库使用不同的对象。
	"""用简单工厂结合反射来代替抽象工厂"""

	db_type = 'SqlServer'		# 选择不同的数据库
	# db_type = 'Oracle'

	def __init__(self):
		user_type = self.db_type + 'User'
		self.user_cls = getattr(__import__('abstract_factory_pattern'), user_type)		# 反射
		dept_type = self.db_type + 'Department'
		self.dept_cls = getattr(__import__('abstract_factory_pattern'), dept_type)
		emp_type = self.db_type + 'Employee'
		self.emp_cls = getattr(__import__('abstract_factory_pattern'), emp_type)

	def create_user(self, name, age, right):
		return self.user_cls(name, age, right)

	def create_department(self, name, prop):
		return self.dept_cls(name, prop)

	def create_employee(self, name, level):		# 新加的对象，直接在 DataAccess 中添加即可。
		return self.emp_cls(name, level)
		
if __name__ == '__main__':
	print('================================')
	db = DataAccess()
	user = db.create_user('Minnie', 25, 'owner')
	user.save()
	dept = db.create_department('tech', 'develop')
	dept.save()
	emp = db.create_employee('Jerry', 1)
	emp.save()







		







