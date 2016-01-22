A = [1,3,5]
B = [2,4,6,8]

# Better get k method by throwing away smaller numbers.

def med(m, n):
	l = len(m) + len(n)
	if l % 2 == 0:
		return (get(m, n, l//2) + get(m, n, l//2+1)) / 2
	return get(m, n, l - l//2)

def get(m, n, k):
	if k != int(k):
		return -1
	k = int(k)
	if m == []: return n[k-1]
	if n == []: return m[k-1]
	if k == 1:
		return min(m[0], n[0])
	t1, t2 = min(len(m)-1, k // 2 - 1), min(len(n)-1, k // 2 - 1)
	if m[t1] >= n[t2]:
		return get(m, n[t2+1:], k-t2-1)
	return get(m[t1+1:], n, k-t1-1)


def findMedianSortedArrays(nums1, nums2):
	def findk(nums1,nums2,k):
		print(nums1,nums2,k)
		if not nums1:
			return nums2[k-1]
		if not nums2:
			return nums1[k-1]
		l1,l2=(len(nums1)+1)/2,(len(nums2)+1)/2
		if l1+l2<=k:
			if nums1[l1-1]<nums2[l2-1]:
				return findk(nums1[l1:],nums2,k-l1)
			else:
				return findk(nums1,nums2[l2:],k-l2)
		else:
			if nums1[l1-1]<nums2[l2-1]:
				return findk(nums1,nums2[:l2-1],k)
			else:
				return findk(nums1[:l1-1],nums2,k)
	ls = len(nums1) + len(nums2)
	ls2 = ls/2
	if ls%2==0:
		return (findk(nums1,nums2,ls2)+findk(nums1,nums2,ls2+1))/2.0
	else:
		return findk(nums1,nums2,ls2+1)

print(findMedianSortedArrays(A,B))