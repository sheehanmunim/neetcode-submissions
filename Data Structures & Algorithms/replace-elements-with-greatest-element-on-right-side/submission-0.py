class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        #reverse itteration
        #new max is old max and previous postion in array

        rightMax = -1

        for i in range(len(arr) - 1 , -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax

        return arr

