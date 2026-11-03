# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Helper to get list length
        def get_len(node):
            count = 0
            while node:
                count += 1
                node = node.next
            return count

        # Ensure l1 is the longer list so we can modify it in-place
        if get_len(l1) < get_len(l2):
            l1, l2 = l2, l1

        def add(l1, l2, cr):
            # Base case: if l1 is finished, check if there's a leftover carry
            if l1 is None:
                return ListNode(cr) if cr else None

            # Shorter list value: use l2.val if it exists, otherwise 0
            v2 = l2.val if l2 else 0

            total = l1.val + v2 + cr
            l1.val = total % 10
            cr = total // 10

            l2_next = l2.next if l2 else None
            l1.next = add(l1.next, l2_next, cr)
            return l1

        return add(l1, l2, 0)