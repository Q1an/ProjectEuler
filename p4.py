# pure brute-force
def ispalindrome(a):
	if str(a)==str(a)[::-1]:
		return True
	return False
rt = 0
for a in xrange(100,1000):
	for b in xrange(100,1000):
		if ispalindrome(a*b):
			rt = max(rt,a*b)
print(rt)