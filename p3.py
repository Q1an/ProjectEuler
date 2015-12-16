#For generate next prime, can use +=2 to double the speed.
from math import sqrt
'''
def prime(n):
    lis = [False,False] + [True] * (n-1)
    for i in xrange(2,n+1):   
        if lis[i]:
            k = i*2
            while k <= n:
                lis[k] = False
                k = k+i
    ans = []    
    for i in xrange(2,n+1):
        if lis[i]:
        	ans.append(i)
    return ans
'''
n = 600851475143
def isprime(ans,n):
    up = sqrt(n)
    for p in ans:
        if p > up:
            return True
        if n%p == 0:
            return False
    return True
def getnextprime(ans,n):
    while(not isprime(ans,n)):
        n +=1
    return (ans+[n],n)
plst = []
a = 1
while(n!=1):
    plst, a = getnextprime(plst,a+1)
    while n%a==0:
        n /= a
print a
