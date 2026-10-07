class Solution(object):
    def findKthPositive(self, arr, k):
        for num in arr:
            if num <= k:
                k += 1
            else:
                break
        return k