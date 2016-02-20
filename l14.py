class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
        	return ""
        for a in xrange(len(strs[0])):
        	for i in strs:
        		if len(i)<=a or strs[0][a]!=i[a]:
        			return strs[0][:a]
        return strs[0]

class Solution1(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
        	return ""
        if len(strs)==1:
        	return strs[0]
        min = float("inf")
        for i in xrange(len(strs)-1):
        	temp = self.lcp(strs[i],strs[i+1])
        	if temp<min:
        		min=temp
        return strs[0][:min]
    def lcp(self,str1,str2):
    	rt = 0
    	for i in xrange(min(len(str1),len(str2))):
    		if str1[i]==str2[i]:
    			rt+=1
    		else:
    			break
    	return rt
print Solution().longestCommonPrefix(["sdf","sdfewf","sderwf"])