class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s = s.replace(" ", "").lower()
        t = t.replace(" ", "").lower()

        counts = {}

        for ch in s:
            counts[ch] = counts.get(ch,0) + 1

        for ch in t:
            if counts.get(ch, 0) == 0:
                return False
            counts[ch] -= 1

        return True