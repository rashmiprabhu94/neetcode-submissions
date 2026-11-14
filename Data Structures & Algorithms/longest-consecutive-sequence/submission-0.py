class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        element_set = set(nums)
        result=0

        for num in element_set:

            if (num-1) in element_set:
                continue

            next_num = num + 1
            count = 1
            while next_num in element_set:
                count += 1
                next_num += 1

            result = max(result,count)

        return result


        