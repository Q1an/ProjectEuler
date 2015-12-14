a = 2
b = 8
s = 0
while a < 4000000:
	s += a
	a, b = b, 4*b + a
print(s) 