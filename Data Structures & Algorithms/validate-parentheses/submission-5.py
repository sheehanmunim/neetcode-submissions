class Solution:
    def isValid(self, s: str) -> bool:
        
        #.pop
        #.append

        #ideally you look to see if its a closing bracket and then see if the matching is an open and if it is then pop

        stack = [] #this is where we are storing everything and seeing if its empty

        closedBrackets = {')':'(', '}':'{', ']':'['}

        if not s:
            return False


        for c in s:
            if c in closedBrackets: #checks to see if its in the dictionary (a closing bracket)
                if stack and stack[-1] == closedBrackets[c]: #checks to see if the last item in the list matches to the bracket
                    stack.pop() #if it does then pop it
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False