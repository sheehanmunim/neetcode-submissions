class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if rev of t = s then return true

        return sorted(s) == sorted(t)

             