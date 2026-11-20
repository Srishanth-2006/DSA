class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for idx, val in enumerate(nums):
            diff = target - val
            if diff in seen:
                return [seen[diff], idx]
            seen[val] = idx