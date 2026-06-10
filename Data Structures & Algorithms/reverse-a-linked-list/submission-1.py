# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #reverse it 
        #take each thing using val and then get the next and make a new array
        #next.next gives stuff

        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next) #this
            head.next.next = head #this
        head.next = None

        return newHead
            
