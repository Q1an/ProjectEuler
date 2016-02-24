dtl = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

class Solution0:
    def letterCombinations(self, digits):
        if not digits: return []
        return reduce(lambda a, digit: [x + y for x in a for y in dtl[int(digit)]], digits, [''])


class Solution(object):
	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		if not digits:
			return []
		rt = ['']
		for i in digits:
			l,le = len(rt),len(dtl[int(i)])
			rt = le*rt
			for d in xrange(le):
				for t in xrange(l):
					rt[d*l+t]+=dtl[int(i)][d]
		return rt
print Solution0().letterCombinations("27")
		