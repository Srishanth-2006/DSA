# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return
        ft=sl=head
        while ft is not None and ft.next is not None:
            ft=ft.next.next
            md=sl
            sl=sl.next
        md.next=sl.next
        return head
        