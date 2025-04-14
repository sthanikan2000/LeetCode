\\\
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
\\\

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ### using a hash map for reference
        if not head:
            return 
        old_new_ref = {}
        current = head
        while current:
            node = Node(current.val)
            old_new_ref[current]=node
            current = current.next
        for old_node in old_new_ref.keys():
            if old_node.next:
                old_new_ref[old_node].next = old_new_ref[old_node.next]
            if old_node.random:
                old_new_ref[old_node].random = old_new_ref[old_node.random]
        return old_new_ref[head]
        