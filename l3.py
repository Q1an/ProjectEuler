def lengthOfLongestSubstring(s):
	ht,st,longest={},0,0
	for i, j in enumerate(s):
		if j in ht and ht[j] >= st:
			st+=ht[j]+1
		ht[j] = i
		longest=max(longest,i-st+1)
	return longest
print(lengthOfLongestSubstring("abcabcaaaaaabb"))