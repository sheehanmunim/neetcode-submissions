# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val <= list2.val: #checks which head is smaller
            list1.next = self.mergeTwoLists(list1.next,list2) #sets list 1 from the next value and all of list2
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


        #ok let's run throgh it
        #list1=[1,2,4]
        #list2=[1,3,5]

        #sees that its the same. so now it makes input [2,4] amd [1,3,5] and 1 is pointing to it
        #now it sees 1 is less than 2 so now it does 1 from list2 which points to the new thing from [2,4] and [3,5]
        #now sees 2 is less than 3 so 2 points to the next thing from [3,5]

        #finaly list1 will return givin new sorted list




