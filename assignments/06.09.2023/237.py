class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node is None:
            return
        
        next_node = node.next
        if next_node is not None:
            
            node.val = next_node.val
            
            node.next = next_node.next