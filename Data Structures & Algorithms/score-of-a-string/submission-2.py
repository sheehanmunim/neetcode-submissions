class Solution:
    def scoreOfString(self, s: str) -> int:
        
        #covernt to ascii and then do abs of first and second and so scoreOfString

        count = 0

        for i in range(len(s) - 1):

            count += abs(ord(s[i]) - ord(s[i + 1]))

        return count