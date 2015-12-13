def sumupto(base,limit):
	return (limit/base+1)*(limit/base)/2*base
up = 1000 - 1
print(sumupto(3,up)+sumupto(5,up)-sumupto(15,up))