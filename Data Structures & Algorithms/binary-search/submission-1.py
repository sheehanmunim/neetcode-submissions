class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #binary search. find the index of target and ouput otherwise output -1
        #do this by going through each

        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1