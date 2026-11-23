class Solution(object):
    def reverseList(self, head):
        def recur(curr, prev):
            # Base case: reached the end of the list, so prev is the new head
            if curr is None:
                return prev
            
            next_node = curr.next   # 1. Save the next node
            curr.next = prev        # 2. Point current node backward to prev
            return recur(next_node, curr)  # 3. Recurse with (next_node, curr)

        return recur(head, None)