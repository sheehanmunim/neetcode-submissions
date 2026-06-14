# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #do this by first having a previous thing set to none

        #then you can change the pointer of the first head to the previous
        #then set the next value as the current value and cycle until you reach the last and head is null

        curr = head
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev #changes the pointer
            prev = curr
            curr = nxt
        return prev