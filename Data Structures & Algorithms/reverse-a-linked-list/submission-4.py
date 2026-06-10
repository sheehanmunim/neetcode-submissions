# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #pointers
        #have first pointer and second pointer

        prev, curr = None, head

        while curr:
            nxt = curr.next #sets next value to 1
            curr.next = prev #sets the pointer to the previous value
            prev = curr
            curr = nxt
            

         
        return prev

        #curr is 0
        #nxt is now 1
        #prev = 0
        #curr.next is 1 and is the new current
        #curr is now 1


