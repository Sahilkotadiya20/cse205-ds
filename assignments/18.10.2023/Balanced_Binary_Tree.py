# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def sample(root):
            if not root:
                return 0
            lh = sample(root.left)
            if lh == -1:
                return -1
            rh = sample(root.right)
            if rh == -1:
                return -1
            if abs(lh-rh)>1:
                return -1
            else: 
                return 1+max(lh,rh)
            
        return sample(root)!=-1