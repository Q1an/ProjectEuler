class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,num,r,m=len(nums),sorted(nums),[],float("inf")
        for i in range(l-2):
        	if i == 0 or num[i]!=num[i-1]:
        		le,ri=i+1,l-1;
        		while le<ri:
        			dif = num[le]+num[ri]+num[i]-target
        			if dif>0:
        				if dif<m:
        					r = [num[i],num[le],num[ri]]
        					m = dif
        				ri-=1
        			elif num[le]+num[ri]+num[i]-target==0:
        				return target
        			else:
        				if -dif<m:
        					r = [num[i],num[le],num[ri]]
        					m = -dif
        				le+=1
        return r[0]+r[1]+r[2]
print Solution().threeSumClosest([-1, 2, 1, -4], 1)