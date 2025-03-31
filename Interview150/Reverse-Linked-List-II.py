# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        current = head
        i = 1
        correct = None
        while i!=left:
            correct = current
            current=current.next

            i+=1
        
        prev = None
        first_prev = None
        while current and i<=right:
            temp = current
            current=current.next
            temp.next = prev
            prev = temp
            i+=1
            if first_prev == None:
                first_prev  = prev
        if correct:
            correct.next = prev
        else:
            head = prev
        if first_prev:
            first_prev.next = current
        return head

        