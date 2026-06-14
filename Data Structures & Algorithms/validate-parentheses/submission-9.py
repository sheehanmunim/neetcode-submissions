class Solution:
    def isValid(self, s: str) -> bool:
        
        #have an inital array.

        #if the value isnt a closing bracket add it to the array
        #check to see if the outer array matches the closed braket array
        #if it does then pop the inner array since it does match


        stack = []
        closedBracket = {')':'(', '}':'{', ']':'['}

        for i in s:
            if i in closedBracket:
                if stack and closedBracket[i] == stack[-1]:
                    stack.pop()
                else:
                    return False


            else:
                stack.append(i)

        return True if not stack else False