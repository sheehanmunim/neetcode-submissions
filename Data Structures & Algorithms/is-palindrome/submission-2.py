class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #isalnum()

        #get every character and make it into a new str. reverse it and see if it works

        newStr = ''

        for i in s:
            if i.isalnum():
                newStr = newStr + i.lower()
        return newStr == newStr[::-1]
