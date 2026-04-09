class Solution:
    def threeSum(self, nums):
        res = []
        s = sorted(nums)
        n = len(s)
        for i in range(n):
            if i > 0 and s[i] == s[i-1]:   # skip doublons sur i
                continue
            l, r = i + 1, n - 1
            while l < r:
                target = s[i] + s[l] + s[r]
                if target < 0:
                    l += 1
                elif target > 0:
                    r -= 1
                else:
                    res.append([s[i], s[l], s[r]])
                    while l < r and s[l] == s[l+1]:  # skip doublons sur l
                        l += 1
                    while l < r and s[r] == s[r-1]:  # skip doublons sur r
                        r -= 1
                    l += 1
                    r -= 1
        return res