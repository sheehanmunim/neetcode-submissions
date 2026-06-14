# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        #do this by going to the left and the right and setting the left to the right and right ot he left

        #then recrun by this time have it so its calling from the left and the right

        if not root:
            return None

        #how can I loop?
        nxt = root.left
        root.left = root.right
        root.right = nxt

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root