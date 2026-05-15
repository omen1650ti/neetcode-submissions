# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sametree(p,q):
            if (p and not q) or (not p and q):
                return False
            if p is None and q is None:
                return True
            if p.val != q.val:
                return False

            return (sametree(p.left,q.left) and sametree(p.right,q.right))
        def has_subtree(node1, subRoot):

            if node1 is None:
                return False
            if sametree(node1,subRoot):
                return True
            return (has_subtree(node1.left,subRoot) or has_subtree(node1.right, subRoot))

        return has_subtree(root, subRoot)

            