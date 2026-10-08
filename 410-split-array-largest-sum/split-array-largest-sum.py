class Solution(object):
    def splitArray(self, nums, k):
        left = max(nums)
        right = sum(nums)
        res = right

        while left <= right:
            mid = left + (right - left) // 2

            # Count how many pieces are needed if max sum <= mid
            pieces = 1
            current_sum = 0
            for x in nums:
                if current_sum + x > mid:
                    pieces += 1
                    current_sum = x
                else:
                    current_sum += x

            if pieces <= k:
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res