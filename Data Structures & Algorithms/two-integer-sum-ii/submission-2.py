class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers) - 1
        l = 0
        while numbers[r] + numbers[l] != target:
            s = numbers[r] + numbers[l]
            if s > target:
                r -= 1
            if target > s:
                l += 1
        return [l+1, r+1]


        