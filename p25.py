a,b,count=1,1,2
def add2(a,b):
	return a+b
while(len(str(b))<1000):
	a,b=b,add2(a,b)
	count +=1
print(b,count)