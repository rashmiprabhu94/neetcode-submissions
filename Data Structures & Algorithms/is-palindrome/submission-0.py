class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s) - 1

        while left < right:
            char_left = s[left].lower()
            char_right = s[right].lower()

            print(char_left, char_right)

            if not char_left.isalnum():
                left += 1
                continue

            if not char_right.isalnum():
                right -= 1
                continue

            if char_left != char_right:
                return False
            
            left += 1
            right -= 1

        return True