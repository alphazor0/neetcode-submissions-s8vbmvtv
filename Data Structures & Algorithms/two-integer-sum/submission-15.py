class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i, num in enumerate(nums):
            presum = target - num
            if presum in seen:
                return [seen[presum], i]
            seen[num] = i
        