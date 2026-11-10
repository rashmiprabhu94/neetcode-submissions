class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        
        for word in strs:
            length = len(word)
            encodedStr += str(length) + '#' + word

        return encodedStr

    def decode(self, s: str) -> List[str]:
        decodedList=[]

        countStr = ""
        i = 0
        while i < len(s):
            if s[i] == '#':
                left = i+1
                right = i+1+int(countStr)
                decodedList.append(s[left:right])
                i = right
                countStr = ""
            else:
                countStr += s[i]
                i += 1

        return decodedList
