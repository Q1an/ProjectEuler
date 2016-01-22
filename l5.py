class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = self.preprocess(s)
        # st = "^" + "".join(list(s)) + "$"
        p = [0] * len(st)
        i,r = 0,1
        for k in xrange(1,len(st)-1):
        	if k<i+p[i]:
        		p[k] = min(r-k,p[2*i-k])
        	else:
        		p[k] = 1
        	while(st[k+p[k]]==st[k-p[k]]):
        		p[k]+=1
        	if p[k]+k>r:
        		i,r=k,k+p[k]
        maxvalue, maxindex = 0,0
        for k in xrange(1,len(st)-1):
        	if p[k]>maxvalue:
        		maxvalue, maxindex = p[k],k
        return s[(maxindex-maxvalue)/2:(maxindex-maxvalue)/2+maxvalue-1]
    def preprocess(self,s):
    	if not s:
    		return "^$"
    	rt = "^"
    	for i in s:
    		rt = rt + "#" + i
    	rt += "#$"
    	return rt
print Solution().longestPalindrome("1122332212")