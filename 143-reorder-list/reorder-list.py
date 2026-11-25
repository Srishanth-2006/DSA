class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        arr = []
        curr = head
        while curr is not None:
            arr.append(curr)
            curr = curr.next

        i = 0
        j = len(arr) - 1
        while i < j:
            arr[i].next = arr[j]
            i += 1
            arr[j].next = arr[i]
            j -= 1
            if i > j:
                break

        arr[i].next = None    # <-- Cuts the cycle on the final node!