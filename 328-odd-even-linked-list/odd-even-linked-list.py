class Solution(object):
    def oddEvenList(self, head):
        l1 = ListNode(0)      # Tail pointer for even-indexed nodes
        l2 = ListNode(0)      # Tail pointer for odd-indexed nodes
        even_head = l1        # Save start of even list
        odd_head = l2         # Save start of odd list

        while head is not None and head.next is not None:
            l2.next = head
            l2 = l2.next
            head = head.next

            l1.next = head
            l1 = l1.next
            head = head.next

        # Attach the final odd node if the list has an odd number of nodes (e.g., node 5)
        if head is not None:
            l2.next = head
            l2 = l2.next

        l1.next = None              # End the even list so it doesn't point back to node 5
        l2.next = even_head.next    # Attach the even list after the odd list
        return odd_head.next