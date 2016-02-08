class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0: 
            return 0
        elif x > 0: 
            t = 1
        elif x < 0: 
            t = -1; x = -x
        rt = 0

        while (x>0):
            rt=rt*10+x%10
            x/=10
        if rt > 2147483647:
            return 0
        return t*rt
        
print Solution().reverse(123)