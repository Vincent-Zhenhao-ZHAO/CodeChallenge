# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            if l1:
                value1 = l1.val
            else:
                value1 = 0
            if l2:
                value2 = l2.val
            else:
                value2 = 0
            sum_num = value1 + value2 + carry
            carry = sum_num // 10
            sum_num = sum_num % 10
            
            current.next = ListNode(sum_num)
            
            current = current.next
            if l1:
                l1 = l1.next
            else:
                l1 = None
            if l2:
                l2 = l2.next
            else:
                l2 = None
        
        return dummy.next