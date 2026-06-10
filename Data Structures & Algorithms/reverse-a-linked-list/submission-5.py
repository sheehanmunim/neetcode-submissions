# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev, curr = None, head

        while curr:
            nxt = curr.next #the next value (1)
            curr.next = prev #sets the pointer of 0 to previous
            prev = curr #the current value now becomes the previous value
            curr = nxt #current value becomes the next value (1)
        return prev