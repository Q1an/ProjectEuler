e = {"I":1, "VI":4, "V":5, "XI":9, "X":10, "LX":40, "L":50, "CX":90, "C":100, "DC":400, "D":500, "MC":900, "M":1000}
k = ["I","VI","V","XI","X","LX","L","CX","C","DC","D","MC","M"]
class Solution(object):
	def romanToInt(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		s,rt=s[::-1],0
		while len(s)>0:
			for i in k:
				while s[:len(i)]==i:
					rt += e[i]
					s = s[len(i):]
		return rt
print Solution().romanToInt("XXX")