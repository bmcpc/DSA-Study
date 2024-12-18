# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
for each node, we need to swap the left and right nodes
recursively traverse, and then swap

base case: when node is null (leaf node), we return 
'''
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        
        swap = root.right
        root.right = root.left
        root.left = swap

        self.invertTree(root.right)
        self.invertTree(root.left)

        return root