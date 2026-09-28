class Solution(object):
    def minDays(self, bloomDay, m, k):
        if m * k > len(bloomDay):
            return -1
        l, r = min(bloomDay), max(bloomDay)
        res = -1
        while l <= r:
            mid = l + (r - l) // 2
            ans = 0
            flowers = 0
            for day in bloomDay:
                if day <= mid:
                    flowers += 1
                    if flowers == k:
                        ans += 1
                        flowers = 0
                        if ans == m:
                            break
                else:
                    flowers = 0
            if ans >= m:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res