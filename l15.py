# no duplication
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """	
        l,num,r=len(nums),sorted(nums),[]
        for i in range(l-2):
        	if i == 0 or num[i]!=num[i-1]:
        		le,ri=i+1,l-1;
        		while le<ri:
        			if num[le]+num[ri]+num[i]>0:
        				ri-=1
        			elif num[le]+num[ri]+num[i]==0:
        				r.append([num[i],num[le],num[ri]])
        				if num[le]==num[ri]:
        					break
        				else:
        					le , ri = le+1, ri-1
        					while num[le]==num[le-1] and le<ri:
        						le+=1
        					while num[ri]==num[ri+1] and ri>le:
        						ri-=1
        			else:
        				le+=1
        return r

class Solution1(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """	
        nums.sort()
        l,d,r = len(nums),{},[]
        if l<=2:
        	return []
        for i in xrange(l):
        	d[nums[i]]=i
        for a in xrange(l):
        	for b in xrange(a+1,l):
        		if (-nums[a]-nums[b]) in d:
        			if d[-nums[a]-nums[b]]>b:
        				r.append([nums[a],nums[b],-nums[a]-nums[b]])
       	return r
print Solution().threeSum([13,9,1,12,-7,-12,7,3,9,6,-7,4,9,5,5,-7,4,11,1,-2,12,3,-12,-15,0,-12,-6,-1,7,-5,-4,-3,12,4,-14,-10,-1,8,1,-6,-1,9,13,-14,-1,-5,-6,-12,-8,2,2,11,13,-3,11,-2,1,-10,4,-15,-8,7,-11,11,-4,-10,-13,3,5,3,12,11,-11,2,12,3,13,13,-2,12,-7,-15,8,-9,-10,-4,-4,6,1,-15,-2,0,-1,2,-3,10,-1,-9,-10,-11,1,-13,-15,5,-3,5,-7,-5,-5,6,14,3,-1,7,1,-4,-12,12,-13,-4,4,0,3,-12,9,-15,6])
