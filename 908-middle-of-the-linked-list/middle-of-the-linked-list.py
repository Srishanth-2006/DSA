# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ft=sl=head
        while(ft!=None and ft.next!=None):
            ft=ft.next
            sl=sl.next
            ft=ft.next
        return sl
        