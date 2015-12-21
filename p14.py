limit,m,ht,mv = 1000000,0,{},0
for a in range(1,limit+1):
	o,t=a,1
	while a!=1:
		if a in ht:
			t+=ht[a]-1
			break
		t += 1
		if a%2 == 0:
			a //= 2
		else:
			a = 3*a + 1
	ht[o]=t
	if t > m:
		m,mv = t,o
print(mv)