# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=0
        dummy=cur=head
        while cur:
            l+=1
            cur=cur.next 

        rem=l-n
        ac=0

        if rem==0:
            return head.next


        while ac!=rem:
            #here can I use cur again to refer to head? I think I can only when I assign head specifically to this value right?
            prev=head
            head=head.next
            ac+=1

        prev.next=head.next
        return dummy        




