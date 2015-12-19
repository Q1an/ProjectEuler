t = 1000
for a in range(1,t//3+1):
	for b in range(a,(t-a)//2+1):
		if a*a + b*b == (t-a-b)*(t-a-b):
			print(a,b,t-a-b)
			break