class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
        	return False
        xcopy,reverse = x,0
        while xcopy:
        	reverse =xcopy%10+reverse*10
        	xcopy /=10
        return reverse==x


print Solution().isPalindrome(12321)