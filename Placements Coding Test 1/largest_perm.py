# largest_perm
N, K =map(int, raw_input().strip().split(' '))
A = map(int, raw_input().strip().split(' '))
if all(A[i] >= A[i+1] for i in xrange(len(A)-1)):
	answer = A
else:
	B = sorted(A)
	B.reverse()
	if K>=N-1:
		answer = B
	else:
		answer =B[:K]
		for i in xrange(K):
			A[A.index(answer[i])] = A[i]
		answer = answer + A[K:]	
print ' '.join(map(str,answer))
