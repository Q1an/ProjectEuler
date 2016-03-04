class Solution(object):
    def gp(self,list,str,l,r):    			
    	if r==0:
    		list.append(str)
    	if l>0:
    		self.gp(list,str+"(",l-1,r)
    	if r>l:
    		self.gp(list,str+")",l,r-1)
    def generateParenthesis(self, n):
        rt = []
        self.gp(rt,"",n,n)
        return rt     

class Solution1(object):
    def generatepartialParenthesis(self,ls,str,l,r):    			
    	if r==0:
    		ls.append(str)
    	elif l==0:
    		ls.append(str+")"*r)
    	elif r==l:
    		self.generatepartialParenthesis(ls,str+"(",l-1,r)
    	else:
	    	self.generatepartialParenthesis(ls,str+"(",l-1,r)
	    	self.generatepartialParenthesis(ls,str+")",l,r-1)
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rt = []
        self.generatepartialParenthesis(rt,"",n,n)
        return rt
# class Solutionwrong(object):
#     def generateParenthesis(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
#         rt = []
#         if n>=1:
#         	rt = ["()"]
#         for i in range(n-1):
#         	l = len(rt)
#         	rt = rt * 3
#         	for k in range(l):
#         		rt[k]="()"+rt[k]
#         		rt[k+l]=rt[k+l]+"()"
#         		rt[k+2*l]="("+rt[k+2*l]+")"
#         	rt = rt[:l]+rt[l+1:]
#         return rt
print Solution().generateParenthesis(4)
# print Solution().generateParenthesis(2)
# print Solution().generateParenthesis(3)
