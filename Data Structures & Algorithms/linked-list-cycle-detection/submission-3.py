# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        #see if it points to none or if it keeps going
        #try doing a hashmap

        seen = set()

        cur = head



        while cur:
            if cur in seen:
                return True
            seen.add(cur)
            cur = cur.next
        return False

        
        