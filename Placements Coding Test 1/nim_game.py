# nim_game
G = int(raw_input().strip())
for g in xrange(G):
	N = int(raw_input().strip())
	S = map(int, raw_input().strip().split(' '))
	answer =0
	for el in S:
		answer = answer^el
	if answer:
		print "First"
	else:
		print "Second"
