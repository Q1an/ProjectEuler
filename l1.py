test = [2,7,11,15]

def twoSum(nums, target):
        ht={}
        for i in xrange(len(nums)):  #For python 2.x using xrange; 3.x using range
			if ht.get(target-num[i], None) == None:
                ht[num[i]] = i
            else:
                return (ht[target-num[i]] + 1, i + 1)


print(twoSum(test,9))
