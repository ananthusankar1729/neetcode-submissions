# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t1, t2 = l1, l2
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while t1 or t2:
            sum = carry
            if t1:
                sum = sum + int(t1.val)
            if t2:
                sum = sum + int(t2.val)
            newNode = ListNode(sum%10)
            carry = sum//10
            curr.next = newNode
            curr = curr.next
            if t1:
                t1 = t1.next
            if t2:
                t2 = t2.next
        
        if carry:
            newNode = ListNode(carry)
            curr.next = newNode
            curr = curr.next
        return dummy.next
            