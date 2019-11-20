# coding: utf-8
'''
	组合模式：对对象组合成的“部分-整体”的层次结构，实现统一的操作方法。
'''

import abc

class IDisplay(abc.ABC):
	"""docstring for IDisplay"""
	@abc.abstractmethod
	def display(self, depth):
		'''abstract'''


class Department(IDisplay):
	"""docstring for IDepartment"""
	def __init__(self, name):
		self.name = name
		self.subdepartments = []
		self.employees = []

	def add_subdepartment(self, department):
		self.subdepartments.append(department)

	def remove_subdepartment(self, department):
		if department in self.subdepartments:
			self.subdepartments.remove(department)

	def add_employee(self, employee):
		self.employees.append(employee)

	def remove_employee(self, employee):
		if employee in self.employees:
			self.employees.remove(employee)
	
	def display(self, depth):
		print('\t'*depth, 'Department:', self.name)
		depth += 1
		for employee in self.employees:
			employee.display(depth)
		for department in self.subdepartments:
			department.display(depth)


class Employee(IDisplay):
	"""docstring for Employee"""
	def __init__(self, name):
		super(Employee, self).__init__()
		self.name = name

	def display(self, depth):
		print('\t'*depth, 'Employee:', self.name)
		


if __name__ == '__main__':
	dept1 = Department('技术中心')
	dept2 = Department('基础运维')
	dept1.add_subdepartment(dept2)
	dept1.add_subdepartment(Department('业务运维'))
	dept1.add_subdepartment(Department('业务开发'))
	dept2.add_subdepartment(Department('portal'))

	emp1 = Employee('jerry')
	emp2 = Employee('giggs')
	dept1.add_employee(emp2)

	emp1.display(1)
	dept1.display(1)

















