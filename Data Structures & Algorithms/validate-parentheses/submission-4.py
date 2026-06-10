class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        #.pop
        #.append

        for i in s:
            if i in closeToOpen: #if its a closed bracket
                if stack and stack[-1] == closeToOpen[i]: #sees if stuff in stack and if that first value matches the close bracket
                    stack.pop()
                else:
                    return False

            else:
                stack.append(i)
        return True if not stack else False