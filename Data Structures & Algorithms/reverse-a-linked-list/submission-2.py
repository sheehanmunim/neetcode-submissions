# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #reverse it 
        #take each thing using val and then get the next and make a new array
        #next.next does

        if not head:
            return None

        newHead = head #current head will become the next head

        if head.next: #value of next node
            newHead = self.reverseList(head.next) #if it returns somethning in the node then make it the new head
            head.next.next = head #this reverses
        head.next = None

        return newHead
            
