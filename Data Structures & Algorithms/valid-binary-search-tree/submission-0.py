# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(low, node: Optional[TreeNode], high):
            if node is None:
                return True
            if not low< node.val < high:
                return False
            
            
            return(validate(low, node.left, node.val) and validate(node.val, node.right, high))

        return validate(float('-inf'), root, float('inf'))
            

        