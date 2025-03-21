# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode(
            val = (l1.val + l2.val)%10
        )
        current = new_head
        carry = (l1.val + l2.val) // 10
        l1 = l1.next
        l2 = l2.next

        while l1 and l2:
            add = l1.val + l2.val + carry
            temp = ListNode(
                val = add%10
            )
            current.next = temp
            current = temp
            carry = add//10
            l1 = l1.next
            l2 = l2.next
        while l1:
            add = l1.val + carry
            temp = ListNode(
                val = add%10
            )
            current.next = temp
            current = temp
            carry = add//10
            l1 = l1.next
        while l2:
            add = l2.val + carry
            temp = ListNode(
                val = add%10
            )
            current.next = temp
            current = temp
            carry = add//10
            l2 = l2.next
        if carry:
            temp = ListNode(
                val = 1
            )
            current.next = temp

        return new_head






