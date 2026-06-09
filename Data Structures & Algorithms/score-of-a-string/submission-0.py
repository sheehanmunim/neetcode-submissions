class Solution:
    def scoreOfString(self, s: str) -> int:
        

        #first get all the ascii values
        #then get the length of s
        #then do abs of first and second and second and third
        #then add everything together

        result = 0

        for i in range(len(s) - 1):

            result += abs(ord(s[i]) - ord(s[i + 1]))

        return result