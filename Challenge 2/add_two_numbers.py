#https://leetcode.com/problems/two-sum/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2:[ListNode]) -> [ListNode]:
        l3 = ListNode(0)
        current_l3 = l3 
        carry = 0
        
        while l1 is not None or l2 is not None or carry != 0:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            
            total = val1 + val2 + carry

            carry = total // 10
            
            current_l3.next = ListNode(total % 10)
            
            current_l3 = current_l3.next
            
            if l1 is not None: l1 = l1.next
            if l2 is not None: l2 = l2.next
        
        return l3.next
