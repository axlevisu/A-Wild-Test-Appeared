from math import factorial
from collections import Counter

N = int(raw_input().strip())
P = map(int, raw_input().strip().split(' '))
if all(P[i] <= P[i+1] for i in xrange(len(P)-1)):
	print 0.0
else:
	Q = Counter(P).values()
	p = factorial(N)*1.0
	for q in Q:
		p = p/factorial(q)

	# answer = p/((1-p)**2)
	print p