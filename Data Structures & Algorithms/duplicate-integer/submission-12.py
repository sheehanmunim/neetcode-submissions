class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        #if more than once return true

        #how will you do this

        #pseud code

        #go through each
        #hashset
        #if seen in hasset then true

        hashSet = set()

        for i in range(len(nums)):
            if nums[i] in hashSet:
                return True
            else:
                hashSet.add(nums[i])
        return False