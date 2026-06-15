class Solution:
    def isValid(self, s: str) -> bool:

        #check if its an. opening or a closing bracket. if its a closing bracket check to see if it matches
        #otherwise add to the stack. pop it out of the stack if it matches
        
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