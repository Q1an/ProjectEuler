class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r,m=0,len(height)-1,0
        while l!=r:
        	if (height[r]>height[l]):
        		m=max(m,(r-l)*height[l])
        		l+=1
        	else:
        		m=max(m,(r-l)*height[r])
        		r-=1
        return m

height = [1,2,3,4,5,3,2,1]
print Solution().maxArea(height)