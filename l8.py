class Solution(object):
	def myAtoi(self, str):
		INT_MAX =  2147483647
		INT_MIN = -2147483648
		rt,sign,i = 0,1,0
		if not str:
			return rt
		while i<len(str) and str[i]==" ":
			i+=1
		if str[i]=="+":
			i+=1
		elif str[i]=="-":
			i+=1
			sign = -1
		while i < len(str) and str[i] >= '0' and str[i] <= '9':	
				rt=10*rt+ord(str[i])-ord('0')
				if rt>INT_MAX:
					return INT_MAX if sign > 0 else INT_MIN
				i+=1
		return sign*rt
print Solution().myAtoi("123")