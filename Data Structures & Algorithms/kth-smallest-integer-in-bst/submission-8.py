# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        m=[]
        def inorder(node):
            
            if node:
                inorder(node.left)
                m.append(node.val)
                inorder(node.right)
            return m
        h=inorder(root)
        for i in range(0,k):
            p=heapq.heappop(h)
        return p

        