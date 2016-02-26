class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        d = ListNode(-1)
        d.next = head
        first,second = d,d
        for i in xrange(n):
        	first = first.next
        while first.next != None:
        	first, second = first.next, second.next
        second.next=second.next.next;
        return d.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
    
print Solution().removeNthFromEnd(head, 1)