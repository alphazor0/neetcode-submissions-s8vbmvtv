class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxvolume = 0
        if not heights:
            return 0
        while r > l:
            v = min(heights[l], heights[r]) * (r - l)
            maxvolume = max(v, maxvolume)
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1
        return maxvolume