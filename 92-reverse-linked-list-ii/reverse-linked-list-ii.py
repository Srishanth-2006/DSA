class Solution(object):
    def reverseBetween(self, head, left, right):
        if head is None or head.next is None or left == right:
            return head

        # Special case: reversal starts at the very first node (head)
        if left == 1:
            prev = None
            h3 = head
            for _ in range(right):
                p1 = head.next
                head.next = prev
                prev = head
                head = p1
            h3.next = head
            return prev

        # Your exact code for left > 1
        h1 = head
        left -= 1
        right -= 1
        cnt = 0
        while cnt < left - 1:
            head = head.next
            cnt += 1
        prev = None
        h2 = head
        head = h3 = head.next
        for i in range(right - left + 1):
            p1 = head.next
            head.next = prev
            prev = head
            head = p1
        h3.next = p1
        h2.next = prev
        return h1