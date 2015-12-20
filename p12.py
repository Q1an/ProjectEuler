from math import sqrt
'''
up = 1000    
lis = [False,False] + [True] * (up-1)
sqr = int(sqrt(up))
for i in xrange(2,sqr):   
    if lis[i]:
        k = i*2
        while k <= up:
            lis[k] = False
            k = k+i 
lst = []
for i in xrange(2,up+1):
    if lis[i]:
    	lst.append(i)
print(lst)
'''
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
        n += 2
    return (ans+[n],n)
plst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 961, 967, 971, 977, 983, 991, 997]
a = 1001
limit = 500
st = 1
cur = 1
while(True):
	cur += 1
	div,n = 1,st
	for p in plst:
		if n == 1:
			break
		k = 1
		while n%p==0:
			n //= p
			k += 1
	   	div *= k
	while n!=1:
		plst, a = getnextprime(plst,a+2)
		k = 1
		while n%a==0:
			n //= a
			k += 1
		div *= 1
	if div > limit:
		print(st)
		break
	st += cur
print(plst)
