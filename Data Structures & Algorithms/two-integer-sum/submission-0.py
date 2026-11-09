class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueIndexMap = {}

        for i, val in enumerate(nums):
            need = target - val

            if need in valueIndexMap:
                return [valueIndexMap[need], i]
            
            valueIndexMap[val] = i