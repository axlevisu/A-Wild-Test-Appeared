# stock_maximize
T = int(raw_input().strip())
for t in xrange(T):
	N = int(raw_input().strip())
	P = map(int, raw_input().strip().split(' '))
	profit =0
	buy =[]
	prev = 0
	P.reverse()
	for p in P:
		if p >=prev:
			buy = [0] + buy
			prev = p
		profit += prev - p 
	print profit
