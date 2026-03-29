# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False
        #If a node is null, I won't be able to comare it's val right? 

        if p.val==q.val:
            
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        return False


        