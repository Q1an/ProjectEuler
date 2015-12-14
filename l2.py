class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
# dummy at the start
# //= v.s. /=
# one sum
def addTwoNumbers(l1, l2):
    dummy = ListNode(0)
    current, sum = dummy, 0
    while l1 != None or l2 != None:
        if l1 != None:
            sum += l1.val
            l1 = l1.next
        if l2 != None:
            sum += l2.val
            l2 = l2.next
        current.next = ListNode(sum%10)
        sum //= 10
        current = current.next
    if sum == 1:
        current.next = ListNode(1)
    return dummy.next        
'''
def addTwoNumbers(l1, l2):
    ret = ListNode(0)
    cur = ret
    sum = 0
    while True:
        if l1 != None:
            sum += l1.val
            l1 = l1.next
        if l2 != None:
            sum += l2.val
            l2 = l2.next
        cur.val = sum % 10
        sum /= 10 #difference between /= and //=
        if l1 != None or l2 != None or sum != 0:
            cur.next = ListNode(0)
            cur = cur.next
        else:
            break
    return ret
'''
l1 = ListNode(0)
l2 = ListNode(1)
print(addTwoNumbers(l1,l2).val,addTwoNumbers(l1,l2).next)