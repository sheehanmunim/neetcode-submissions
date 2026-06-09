class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        #first sort and then subtract big vs small
        #creatae new thing and remove others until none left

        while len(stones) > 1:
            stones.sort()
            cur = stones.pop() - stones.pop()
            if cur:
                stones.append(cur)

        return stones[0] if stones else 0
