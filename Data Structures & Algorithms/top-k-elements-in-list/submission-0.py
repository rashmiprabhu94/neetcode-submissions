class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDict = {}

        for val in nums:
            countDict[val] = countDict.get(val, 0) +  1

        bucket = [[] for _ in range(len(nums) + 1)]

        for key,val in countDict.items():
            bucket[val].append(key)
    
        result = []
        for freq in range(len(nums),0,-1):
            for num in bucket[freq]:
                result.append(num)
                if len(result) == k:
                    return result

        return result