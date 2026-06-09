class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #make everything lowercase
        #add all the stuff togeterh
        #flip everything
        #see if it matches before flipping

        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]