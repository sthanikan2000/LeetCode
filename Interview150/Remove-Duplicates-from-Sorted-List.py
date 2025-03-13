# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head:
#             return head
#         head_=head
#         while head_.next and head_.next.val == head_.val:
#             head_=head_.next
#         # Now we have our head

#         if not head_.next:
#             return head_

#         p1 = head_
#         p2 = head_.next 

#         while p2 and p2.next:
#             if p2.val == p2.next.val:
#                 p2 = p2.next
#             else:
#                 p1.next=p2
#                 p1=p2
#                 p2=p2.next
#         p1.next = p2
#         return head_
            
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head 
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head 
