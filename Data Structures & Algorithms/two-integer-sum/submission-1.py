class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dictionary = {}

    

        for i, n in enumerate(nums): #i is the array and n is the value in the array
        #so if nums = [1,2,3]
        #it will give like 0 1
        #1 2
        #2 3
        # i is the index and n is the actual value of that number like 1
            diff = target - n #gives difference between
            #so if target is 9 and n is 2 then diff will be 7

            if diff in dictionary: #sees if value of difference is in input
                return [dictionary[diff], i]
            dictionary[n] = i #stores values in dict as i is the array val and n is the value in the array