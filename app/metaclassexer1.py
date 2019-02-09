# -*- coding:utf-8 -*-

class member_table(dict):
	def __init__(self):
		self.member_names = []
	def __setitem__(self, key, value):
		if key not in self:
			self.member_names.append(key)
		dict.__setitem__(self, key, value)

class OrderedClass(type):
	import pdb; pdb.set_trace()
	@classmethod
	def __prepare__(metaclass, name, bases):
		import pdb;pdb.set_trace()
		return member_table()
	def __new__(cls, classname, bases, classdict):
		result = type.__new__(cls, classname, bases, dict(classdict))
		import pdb; pdb.set_trace()
		result.member_names = classdict.member_names
		return result

class MyClass(metaclass=OrderedClass):
	def method1(self):
		pass
	def method2(self):
		pass

if __name__ == '__main__':
	myclass = MyClass()