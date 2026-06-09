class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # if there is a duplicate then output true, other wise false
        # hash set

        hashset = set()

        for i in range(len(nums)):
            if nums[i] in hashset:
                return True
            else:
                hashset.add(nums[i])
        return False
