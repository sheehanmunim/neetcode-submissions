class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

    #it wants twice?
    #take the array and pop?
    #or to it with a for loop and make a new array

        newArr = []

        for i in range(2): #this makes it so it goes twice?
            for j in nums:
                newArr.append(j)
        return newArr
    