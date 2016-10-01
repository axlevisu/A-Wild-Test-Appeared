# sherlock_planes
from operator import sub

def transpose(alist):
	return map(list, zip(*alist))

T = int(raw_input().strip())
for t in xrange(T):
	points =[]
	apoint = map(int, raw_input().strip().split(' '))
	for i in xrange(3):
		point = map(sub, map(int, raw_input().strip().split(' ')), apoint)
		points.append(point)

	if [0,0,0] in transpose(points):
		print 'YES'
	else:
		print 'NO'