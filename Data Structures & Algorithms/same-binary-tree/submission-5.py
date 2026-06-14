# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        #see if p and q exist. if they dont return true

        #if it does exist then see if the left matches the right
        #do this by going to next and seeing if its the same

        if not p and not q:
            return True

        if p and q and p.val == q.val:

                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


            
            
        else:
                return False
        

