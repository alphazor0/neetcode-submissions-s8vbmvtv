class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        valuetofreq = {}
        res = []
        for i in range(len(nums)):
            valuetofreq[nums[i]] = valuetofreq.get(nums[i], 0) + 1

        sortedbuck = [[] for _ in range(len(nums) + 1)]
        for n in valuetofreq.keys():
            sortedbuck[valuetofreq[n]].append(n)
        
        for i in range(len(sortedbuck) - 1, -1, -1):
            for n in sortedbuck[i]:
                res.append(n)
                if len(res) == k:
                    return res