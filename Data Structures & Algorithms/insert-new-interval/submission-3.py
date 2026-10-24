from bisect import bisect_left

def do_overlap(i1, i2):
    if i1[0] > i2[0]:
        i1, i2 = i2, i1
    a, b = i1
    c, d = i2
    return b >= c

def join(i1, i2):
    a, b = i1
    c, d = i2
    return (min(a,c), max(b,d))

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start = bisect_left(intervals, newInterval[0], key=lambda i: i[0]) - 1
        end = bisect_left(intervals, newInterval[1], key=lambda i: i[1]) 
        
        print(start, end)
        while start >= 0 and do_overlap(intervals[start], newInterval):
            newInterval = join(newInterval, intervals[start])
            start -= 1
        while end < len(intervals) and do_overlap(intervals[end], newInterval):
            newInterval = join(newInterval, intervals[end])
            end += 1
        print(start, end)
        return intervals[:start+1] + [newInterval] + intervals[end:]
