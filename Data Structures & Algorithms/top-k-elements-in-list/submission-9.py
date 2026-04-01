class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        valuetofreq = {}
        for i in range(len(nums)):
            valuetofreq[nums[i]] = valuetofreq.get(nums[i], 0) + 1
        sorted_keys = sorted(valuetofreq, key=valuetofreq.get, reverse=True)

        return sorted_keys[:k]