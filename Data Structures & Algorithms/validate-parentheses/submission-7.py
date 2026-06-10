class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        closed = {')':'(', '}':'{', ']':'['}

        #check to see if its an open or closed paraenthises

        for i in s:
            if i in closed:
                if stack and stack[-1] == closed[i]: #[-1] gives the last thing in the array and see if it matches to the bracket
                    stack.pop()
                else:
                    return False

            else:
                stack.append(i)
        return True if not stack else False