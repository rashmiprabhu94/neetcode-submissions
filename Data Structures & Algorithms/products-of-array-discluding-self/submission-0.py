class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        product = 1

        prefix = []
        for num in nums:
            prefix.append(product)
            product *= num

        product = 1

        result = [0] * len(nums)
        for i in range(len(nums)-1,-1,-1):
            result[i] = product * prefix[i]
            product *= nums[i]

        return result
        