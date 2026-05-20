from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nums = Counter(nums)
        nums = sorted(nums.items(), reverse=True, key= lambda x: x[1])

        result = []

        
        return [num for num, count in nums[:k]]


        