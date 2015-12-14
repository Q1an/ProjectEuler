a, b, s =2, 8, 0
while a < 4000000:
	s += a
	a, b = b, 4*b + a
print(s) 