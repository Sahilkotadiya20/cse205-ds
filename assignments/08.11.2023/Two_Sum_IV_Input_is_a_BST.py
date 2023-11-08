# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.hash = {}
        def dfs(node):
            if node:
                if node.val in self.hash:
                    return True
                self.hash[k - node.val] = 1
                return dfs(node.left) or dfs(node.right)
            
        return dfs(root)