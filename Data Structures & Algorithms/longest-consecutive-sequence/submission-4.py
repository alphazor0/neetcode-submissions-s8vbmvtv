class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        seen = set(nums)
        res = 0
        for n in nums:
            if n - 1 not in seen:
                streak = 1
                while n + streak in seen:
                    streak += 1
                res = max(res, streak)
        return res
        