"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        #ensure no clonflicts
        #do this by checking if anything fals within eachother

        for i in range(len(intervals)): #goes through the stuff
            A = intervals[i] #this is the first interval
            for j in range(i + 1, len(intervals)):
                B = intervals[j]
                if min(A.end, B.end) > max(A.start, B.start): #takes the min of the endand sees if it is larger 
                    return False
        return True



