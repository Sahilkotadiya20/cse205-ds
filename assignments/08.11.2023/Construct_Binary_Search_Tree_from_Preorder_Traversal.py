# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    preorder_index = 0
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        for index, val in enumerate(preorder):
            if index == 0:
                continue

            self.insert(root, val)
        return root

    def insert(self, root, val):
        curr = root
        while curr:
            if curr.val > val:
                if curr.left is None:
                    curr.left = TreeNode(val)
                    break
                curr = curr.left
            if curr.val < val :
                if curr.right is None:
                    curr.right = TreeNode(val)
                    break
                curr = curr.right