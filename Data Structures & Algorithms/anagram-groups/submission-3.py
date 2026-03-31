class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs == [""]:
            return [[""]]
        result = []
        def isanagram(str1, str2):
            if len(str1) != len(str2):
                return False
            map1 = {}
            map2 = {}
            for c in str1:
                map1[c] = map1.get(c, 0) + 1
            for c in str2:
                map2[c] = map2.get(c, 0) + 1
            if map1 == map2:
                return True
            else: return False
        
        visited = set()
        for i in range(len(strs)):
            if i in visited:
                continue
            group = []
            group.append(strs[i])
            visited.add(i)
            for j in range(i + 1, len(strs)):
                if j not in visited and isanagram(strs[i], strs[j]):
                    group.append(strs[j])
                    visited.add(j)
            result.append(group)
        return result

