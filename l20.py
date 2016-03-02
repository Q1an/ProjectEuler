class Solution:
	def isValid(self, s):
		l,D = [],{'}':'{',')':'(',']':'['}
		for i in s:
			if i == '(' or i=='{' or i=='[':
				l.append(i)
			elif i == ')' or i=='}' or i==']':
				if len(l)==0 or l.pop()!=D[i]:
					return False
			print l
		return len(l)==0

print Solution().isValid("()[]{}")
print Solution().isValid("()[{]}")