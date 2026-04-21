from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = []
        temp = list(strs)
        seen = [False] * len(temp)
        for i in range(len(temp)):
            if seen[i]:
                continue
            arr = []
            count_i = Counter(temp[i])
            for j in range(i + 1, len(temp)):
                if seen[j]:
                    continue
                count_j = Counter(temp[j])
                if count_i == count_j:
                    arr.append(temp[j])
                    seen[j] = True
            
            arr.append(temp[i])
            result.append(arr)
            seen[i] = True
        
        return result