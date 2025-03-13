# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        duplicate = head.val == head.next.val
        if duplicate:
            head_=None
            lst = None
            current=head.next
        else:
            head_=head
            lst=head_
            current=head.next

        while current.next:
            if current.val != current.next.val:
                if duplicate:
                    current=current.next
                    duplicate =False
                    if not current.next:
                        if not lst:
                            return current
                        else:
                            lst.next=current
                            return head_
                else:
                    if not lst:
                        head_=current
                        lst = current
                        current=current.next
                    else:
                        lst.next=current
                        lst=lst.next
                        current=current.next
            else:
                duplicate=True
                current=current.next
                if not current.next:
                    if lst:
                        lst.next=None
                    
        return head_





