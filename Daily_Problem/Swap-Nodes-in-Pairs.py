# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        y = head.next
        head.next = y.next
        y.next = head
        head = y

        current = head.next
        while current.next and current.next.next:
            y = current.next.next
            current.next.next = y.next
            y.next = current.next
            current.next  = y
            
            current = current.next.next
        return head

        