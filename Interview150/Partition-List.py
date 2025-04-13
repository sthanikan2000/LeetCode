# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l_head = None
        l_tail = None
        r_head = None
        r_tail = None
        current=head
        while current:
            if current.val < x and  l_head:
                l_tail.next = current
                current = current.next
                l_tail = l_tail.next
                # l_tail.next = None
            elif current.val < x:
                temp = current
                current = current.next
                # temp.next = None
                l_head = l_tail = temp
            elif r_head:
                r_tail.next = current
                current = current.next
                r_tail = r_tail.next
                # r_tail.next = None
            else:
                temp = current
                current = current.next
                # temp.next = None
                r_head = r_tail = temp

        if l_head and r_head:
            l_tail.next = r_head
            r_tail.next = None
        elif r_head:
            return r_head
        return l_head





        