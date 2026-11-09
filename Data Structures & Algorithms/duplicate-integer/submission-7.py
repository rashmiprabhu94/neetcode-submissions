class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        valueSet = set()
        for val in nums:
            if val in valueSet:
                return True
            valueSet.add(val)
        return False