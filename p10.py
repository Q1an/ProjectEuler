from math import sqrt
s,up = 0,2000000    
lis = [False,False] + [True] * (up-1)
sqr = int(sqrt(up))
for i in xrange(2,sqr):   
    if lis[i]:
        k = i*2
        while k <= up:
            lis[k] = False
            k = k+i 
for i in xrange(2,up+1):
    if lis[i]:
    	s+=i
print(s)