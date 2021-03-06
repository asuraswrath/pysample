# -*- coding: utf-8 -*-

import bisect
import sys

haystack = [1, 4, 5, 6, 8, 12, 15, 20 , 21,23 ,23, 26, 29, 30]
needles = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

row_fmt = '{0:3d} @ {1:3d}     {2}{0:<3d}'

def demo(bisect_fn):
	for needle in reversed(needles):
		position = bisect_fn(haystack, needle)
		offset = position * ' |'
		print(row_fmt.format(needle, position, offset))


if __name__ == '__main__':
	if sys.argv[-1]  == 'left':
		bisect_fn = bisect.bisect_left
	else:
		bisect_fn = bisect.bisect_right
	print('DEMO:',bisect_fn.__name__)
	haystack_header = ' '.join(map(lambda x:str(x), haystack))
	print('haystack->', haystack_header)
	#print('haystack ->', ''.join('%3d' % n for n in haystack))
	demo(bisect_fn)