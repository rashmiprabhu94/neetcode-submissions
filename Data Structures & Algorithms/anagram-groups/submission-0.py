from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            countArr = [0] * 26

            for char in word:
                index = ord(char) - ord('a')
                countArr[index] += 1

            key = tuple(countArr)
            groups[key].append(word)

        return list(groups.values())