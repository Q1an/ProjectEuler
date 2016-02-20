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