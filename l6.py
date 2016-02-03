class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s or numRows <=1:
        	return s
        tmp=['' for i in xrange(numRows)]
        index = -1; step = 1
        for i in xrange(len(s)):
        	index += step
        	if index==numRows:
        		index-=2;step=-1
        	if index==0 and step==-1:
        		index=0;step=1
        	tmp[index]+=s[i]
       	print tmp
        return ''.join(tmp)
       	


print Solution().convert("PAYPALISHIRING", 3)