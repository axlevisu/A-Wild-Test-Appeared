# cipher
N = int(raw_input().strip())
P = raw_input().strip()
k = int(raw_input().strip())
answer =""
for p in P:
	n = ord(p)
	if n in range(97,123):
		n = (n+k-97)%26 +97
	if n in range(65,91):
		n =  (n+k-65)%26 +65
	answer = answer + chr(n)
print answer