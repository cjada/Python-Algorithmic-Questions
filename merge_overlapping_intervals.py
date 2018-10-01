# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        intervals.sort(key = lambda x : x.start)
        length = len(intervals) - 1
        i = 0
        while i < length:
            if intervals[i].end >= intervals[i+1].start:
                a = intervals.pop(i)
                b = intervals.pop(i)
                end = b.end
                #print(b.start, b.end)
                if a.end > end:
                    end = a.end
                intervals.insert(i, Interval(a.start, end))
                length -= 1
            else:
                i += 1
                
        return intervals