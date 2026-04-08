class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        sorted_nums = sorted(set(nums))  # set() élimine les doublons
        res = 1
        curr = 1                         # on part à 1, pas 0
        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i+1] == sorted_nums[i] + 1:
                curr += 1
            else:
                res = max(res, curr)
                curr = 1                 # reset à 1, pas 0
        return max(res, curr)            # capture la dernière séquence






        