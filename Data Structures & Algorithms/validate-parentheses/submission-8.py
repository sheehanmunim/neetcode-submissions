class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        closedBracket = {')':'(', '}':'{', ']':'['}

        for i in s:
            if i in closedBracket:
                if stack and stack[-1] == closedBracket[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False