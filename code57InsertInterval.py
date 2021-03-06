"""
57 Insert Interval

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
"""
from Interval import *
from bisect import bisect_left
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals or len(intervals) < 1:
            return [newInterval]
        elif not newInterval:
            return intervals

        # Corner case 1: newInterval.end < intervals[0].start
        if newInterval.end < intervals[0].start:
            intervals.insert(0, newInterval)
            return intervals

        # Corner case 2: newInterval.start > intervals[-1].end
        if newInterval.start > intervals[-1].end:
            intervals.append(newInterval)
            return intervals
        
        res = []
        included = False
        for e in intervals:
            if e.end < newInterval.start: # e is smaller than newInterval
                res.append(e)
            else:
                if not included:
                    res.append(newInterval)
                    included = True
                
                if e.start > newInterval.end:
                    res.append(e)
                else:
                    newInterval.start = min(newInterval.start, e.start)
                    newInterval.end = max(newInterval.end, e.end)
                    
        return res

    # 2nd round solution on 6/2/2019
    def insert2(self, intervals, newInterval):
        # binary search to find the insert position
        i, j = 0, len(intervals)
        while i < j:
            mid = (i + j)//2
            if intervals[mid].start <= newInterval.start:
                i = mid + 1
            else:
                j = mid
        
        # insert newInterval at position j
        intervals.insert(j, newInterval)

        # merge j-1 and j if they overlap
        if j > 0 and intervals[j-1].end >= intervals[j].start:
            intervals[j-1].end = max(intervals[j-1].end, intervals[j].end)
            intervals.pop(j)
            j -= 1
        
        # continue merging until no overlap detected
        while j + 1 < len(intervals) and intervals[j].end >= intervals[j+1].start:
            intervals[j].end = max(intervals[j].end, intervals[j+1].end)
            intervals.pop(j+1)

        return intervals

    # 9/2/2020
    # use bisect_left to find the insert position, then insert the interval
    # Then start from i-1 element, we must check and merge these intervals
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = bisect_left(intervals, newInterval)      
        intervals.insert(i, newInterval)
        while i < len(intervals):
            if i > 0 and intervals[i-1][1] >= intervals[i][0]:
                intervals[i-1][1] = max(intervals[i-1][1], intervals[i][1])
                intervals.pop(i)
            else:
                i += 1
        
        return intervals

obj = Solution()
case, new = [[1,2],[3,5],[6,7],[8,10],[12,16]], Interval(4,8)
case, new = [[3, 5], [6,7], [8, 10], [12, 16]], Interval(1,6)
case, new = [], Interval(1,3)
case, new = [[0,5],[9,12]], Interval(7,16)  # expect [[0, 5], [7, 16]]
intervals = []
for element in case:
    intervals.append(Interval(*element))

print(obj.insert2(intervals, new))
