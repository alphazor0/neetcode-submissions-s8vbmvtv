class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        dict1 = {}
        dict2 = {}
        for i in range(len(s1)):
            dict1[s1[i]] = 1 + dict1.get(s1[i], 0)

        for i in range(len(s1)):
            dict2[s2[i]] = 1 + dict2.get(s2[i], 0)

        for r in range(len(s1), len(s2)):
            if dict1 == dict2:
                return True
            dict2[s2[r]] = 1 + dict2.get(s2[r], 0)
            dict2[s2[r - len(s1)]] -= 1
            if dict2[s2[r - len(s1)]] == 0:
                del dict2[s2[r - len(s1)]]
        return dict1 == dict2


        
        
