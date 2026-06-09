class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        count = 0

        for n in details:
            
            if int(n[11:13]) > 60:
                count += 1

        return count