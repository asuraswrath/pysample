# -*- coding: utf-8 -*-

from collections import deque

def printer():
	counter = 0
	while True:
		string = yield
		print('[{0}]  {1}'.format(counter, string))
		counter += 1

def task(name, times):
	for i in range(times):
		#import pdb; pdb.set_trace()
		yield
		print(name, i)

class Runner:
	def __init__(self, tasks):
		self.tasks = deque(tasks)
		print()

	def next(self):
		return self.tasks.pop()
		print()

	def run(self):
		while len(self.tasks):
			task = self.next()
			try:
				next(task)
			except StopIteration:
				pass
			else:
				self.tasks.appendleft(task)

def main():
	t1 = task('wanghong', 5)
	t2 = task('gelina', 8)
	t3 = task('wangxinyi', 3)
	r = Runner([t1, t2, t3])
	r.run()

if __name__  == '__main__':
	p = printer()
	next(p)
	p.send('hi')
	p.send('my name is wang')
	p.send('bye!')
	main()