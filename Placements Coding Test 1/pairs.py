# pairs
from operator import add
def pairs(a,k):
    #a contains array of numbers and k is the value of difference
    answer = 0
    # a = sort(a)
    # n = len(a)
    a = set(a)
    # b = map(add,a,[k]*n)
    for el in a:
    	if el+k in a: 
    		answer+=1
    return answer
# Tail starts here
if __name__ == '__main__':
    a = map(int, raw_input().strip().split(" "))
    _a_size=a[0]
    _k=a[1]
    b = map(int, raw_input().strip().split(" "))
    print pairs(b,_k)