class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        #excude first 11 characters. then take the next to digits and see if they are greater than 60 and add to countSeniors

        count = 0
        for i in details:

            if int(i[11:13]) > 60:
                count += 1
            
        return count