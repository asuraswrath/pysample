# -*- coding: utf-8 -*-

class OrginalObject:
	def __init__(self, val):
		self.val = val

def proxy(orginal_obj):
	class OrginalObj:
		def __getattribute__(self, name):
			return getattr(orginal_obj, name)
	return OrginalObj()

class MyProperty:
	def __init__(self, fget=None, fset=None, fdelete=None, fdoc= None):
		self.fget = fget
		self.fset = fset
		self.fdelete = fdelete
	def __get__(self, instance, ower):
		return self.fget(instance)
	def __set__(self, instance, value):
		self.fset(instance, value)
	def __delete__(self, instance):
		self.fdelete(instance)

class TestProperty:
	def __init__(self, val=5):
		self._val = val
	def get_value(self):
		return self._val
	def set_value(self, val):
		self._val = val
	def delete_value(self):
		del self._val
	x = MyProperty(get_value, set_value, delete_value)


if __name__ == '__main__':
	oo = OrginalObject(5)
	po =proxy(oo)
	oo.val =3
	po.val =4

	tp = TestProperty()
	tp.x
	tp.x = 3
	tp.x