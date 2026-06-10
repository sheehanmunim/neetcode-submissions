# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev, curr = None, head #previous is null and the curretn value starts at the head

        # head = [0,1,2,3]

        while curr: #curr is 0
            nxt = curr.next #this is storing the next node (1)
            curr.next = prev #this sets the previous not do the next node (the next thing in the node (curr) now points to null (0 now points to null))
            prev = curr #Null becomes 0
            curr = nxt #current becomes 1
            #new thing is now [0 points to null, 0 1 2 3]

            #now let's go through it again
            #curr is 1
            #nxt is 2
            #curr 1 next thing points to 0
            #prev is now 1
            #curr is now 2
            #new thing is now [0 points to null, 1 points to 0, 2 is next thing which is ponit to 3]

            #again
            #curr is 2
            #nxt is 3
            #curr 2 now points to 1
            #prev is now 2
            #current is now 3
            #now 0 points to null, 1 points to 0, 2 points to 1, and 3 points to null

            #finally
            #curr is 3
            #nxt is now null
            #curr 3 now points to 2 since prev was 2
            #prev is now 3
            #curr is now null
            #now everything is pointing correctly
            #if you return prev then it will do 3->2->1->0->null

        return prev