# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ft=sl=head
        while(ft is not None and ft.next is not None):
            ft=ft.next.next
            if(ft==sl):
                return True
            sl=sl.next
        return False
        