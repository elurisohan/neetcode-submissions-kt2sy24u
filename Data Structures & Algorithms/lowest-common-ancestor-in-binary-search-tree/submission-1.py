# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stac=[root]
        while stac:
            nod=stac.pop()
            if p.val<=q.val and q.val>=nod.val and p.val<=nod.val:
                return nod
            elif p.val>=q.val and q.val<=nod.val and p.val>=nod.val:
                return nod
            elif max(p.val,q.val)<nod.val:
                stac.append(nod.left)
            elif max(p.val,q.val)>nod.val:
                stac.append(nod.right)
        
