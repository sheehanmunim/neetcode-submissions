# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        #do this by seeing which side is longer and then returning hte max
        #add 1 since you are starting at head

        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
