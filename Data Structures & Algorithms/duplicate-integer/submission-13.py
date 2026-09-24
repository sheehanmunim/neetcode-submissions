class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        

        #if its in the hashset then true. else fals

        hashSet = set()

        for i in range(len(nums)):

            if nums[i] in hashSet:
                return True
            else:
                hashSet.add(nums[i])
        return False