from math import sqrt
n = 10001
up = 120000     #Solve(x/ln(x)=10001,x)
lis = [False,False] + [True] * (up-1)
sqr = int(sqrt(up))
for i in xrange(2,sqr):   
    if lis[i]:
        k = i*2
        while k <= up:
            lis[k] = False
            k = k+i
ans = []    
for i in xrange(2,up+1):
    if lis[i]:
    	ans.append(i)
print(ans[n-1],len(ans))