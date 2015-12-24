s,r = 1,0
for i in range(1,101):
	s*=i
for k in str(s):
	r+=int(k)
print(r)