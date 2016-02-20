class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        T = [[False for j in xrange(len(p) + 1)] for i in xrange(len(s) + 1)]
        T[0][0] = True
        for z in xrange(1,len(p)+1):
        	if p[z-1]=="*":
        		T[0][z]=T[0][z-2]
        for a in xrange(1,len(s)+1):
        	for b in xrange(1,len(p)+1):
        		if p[b-1]!="*":
        			T[a][b]= T[a-1][b-1] and ( s[a-1]==p[b-1] or p[b-1]==".")
        		else:
        			T[a][b]= T[a][b-2] or (T[a-1][b] and (s[a-1]==p[b-2] or p[b-2]=="."))
        return T[len(s)][len(p)]
class Solution1(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
        	return not s
        if len(p)==1 or p[1]!='*':
        	if len(s)>0 and (s[0]==p[0] or p[0]=='.'):
        		return self.isMatch(s[1:],p[1:])
        	else:
        		return False 
        else:
        	while len(s)>0 and (s[0]==p[0] or p[0]=='.'):
        		if self.isMatch(s,p[2:]):
        			return True
        		s=s[1:]
        	return self.isMatch(s, p[2:])
        
print Solution().isMatch("abab", "a*b*")
print Solution().isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")
print Solution().isMatch("aa","a")
print Solution().isMatch("aa","aa")
print Solution().isMatch("aaa","aa")
print Solution().isMatch("aa", "a*")
print Solution().isMatch("aa", ".*")
print Solution().isMatch("ab", ".*")
print Solution().isMatch("aab", "c*a*b")
print Solution().isMatch("aaa", "a*a")
print Solution().isMatch("ab", ".*c")