# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        deck=collections.deque([root])
        ans=[]
        while deck:
            temp=[]
            le=len(deck)
            for i in range(le):
                node=deck.popleft()
                if node:
                    temp.append(node.val)
                if node.left:
                    deck.append(node.left)
                if node.right:
                    deck.append(node.right)#If I keep incrementing deck length. The loop will continue right? So I'm going to append the ans to deck. 
             
                
            if temp:
                ans.append(temp)
        return ans