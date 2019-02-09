# -*- coding:utf-8 -*-

import cmd, sys
from turtle import *

class TurtleShell(cmd.Cmd):
	intro = 'Welcome to the turtle shell. Try help or ? to list commands.\n'
	prompt = '(turtle)'
	file = None

	# ---basic turtel commands---
	def do_forward(self, arg):
		'Move the turtle forward by specified distance:Forward 10'
		forwrad(*parse(arg))
	def do_right(self, arg):
		'Turn turtle right by given number of degree:right 20'
		right(*parse(arg))
	def do_left(self, arg):
		'Turn turtle left by given number of degree:left 20'
		left(*parse(arg))
	def do_goto(self, arg):
		'Move the turtle to an absolute position with changing orientation:goto 100 200'
		goto(*parse(arg))
	def do_circle(self, arg):
		'Draw circle with given radius an option extent and steps: circle 50'
		circle(*parse(arg))
	def do_position(self, arg):
		'Print the current turtel position:poistion'
		print('Current position is %d %d \n' % position())
	def do_heading(self, arg):
		'print the current turtel heading in degrees:heading'
		print('Current heading is %d \n' %(heading(),))
	def do_color(self, arg):
		'set the color:color blue'
		color(arg.lower())
	def do_bye(self, arg):
		'stop recording, close the turtle window, and exit:bye'
		print('Thank you for using Turtle!')
		self.close()
		bye()
		return True
	# ---record and playback---
	def do_record(self, arg):
		'save future commands to filename:record rose.cmd'
		self.file = open(arg, 'w')
	def do_playback(self, arg):
		'playback commands from a file:playback rose.cmd'
		self.close()
		with open(arg) as f:
			self.cmdqueue.extend(f.read().splitlines())
	def precmd(self, line):
		line = line.lower()
		if self.file and 'playback' not in line:
			print(line, file=self.file)
		return line
	def close(self):
		if self.file:
			self.file.close()
			self.file = None

def parse(arg):
	'convert a series of zero or more number to an argument tuple'
	return tuple(map(int, arg.split()))

if __name__ == '__main__':
	TurtleShell().cmdloop()
