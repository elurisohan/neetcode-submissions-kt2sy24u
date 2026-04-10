# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        deq1=deque([p])
        deq2=deque([q])



        while deq1 and deq2:
            n1=deq1.popleft()
            n2=deq2.popleft()

            if n1 is None and n2 is None:
                continue
            if n1 is None or n2 is None or n1.val != n2.val:
                return False
            deq1.append(n1.left)
            deq1.append(n1.right)
            deq2.append(n2.left)
            deq2.append(n2.right)

        return True


        