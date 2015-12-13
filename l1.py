test = [2,7,11,15]

def twoSum(nums, target):
        ht={}
        for a in xrange(len(nums)):  #For python 2.x using xrange; 3.x using range
            if target-nums[a] in ht:
               return [ht[target-nums[a]]+1,a+1]
            ht[nums[a]]=a

print(twoSum(test,9))
