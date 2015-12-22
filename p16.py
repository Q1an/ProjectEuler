s,r = 1,0
for a in range(1000):
	s*=2
for k in str(s):
	r += int(k)
print(r)