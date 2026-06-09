class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
       


        #just take the list and append it to the end
        for i in range(len(nums)):
            nums.append(nums[i])
        return nums
