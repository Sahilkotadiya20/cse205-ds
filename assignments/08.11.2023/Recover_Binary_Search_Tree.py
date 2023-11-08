# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        
        prev, first, second = None, None, None

        def inorder(node):
            nonlocal prev, first, second

            if node.left:
                inorder(node.left)
            
            if prev and first is None and prev.val>node.val:
                first = prev
            if prev and first is not None and prev.val>node.val:
                second = node
            
            prev = node

            if node.right:
                inorder(node.right)
        
        inorder(root)
        tmp = first.val
        first.val = second.val
        second.val = tmp