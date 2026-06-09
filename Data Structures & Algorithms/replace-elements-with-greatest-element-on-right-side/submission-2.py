class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        

        #set -1 as the last
        #go from last and take max and set the new max

        rightMax = -1

        for i in range(len(arr) - 1, -1, -1):

            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        
        return arr
            