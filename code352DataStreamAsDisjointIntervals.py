"""
352 Data Stream as Disjoint Intervals

Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize the numbers seen so far as a list of disjoint intervals.

For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be:

[1, 1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]
Follow up:
What if there are lots of merges and the number of disjoint intervals are small compared to the data stream's size?
"""
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return '['+str(self.start)+', '+str(self.end)+']'

class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []

    # why this is wrong?
    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        # if intervals is empty, just add [val, val]
        if len(self.intervals) == 0:
            self.intervals.append(Interval(val, val))
            return        

        # find the insertion index for val in start
        start, end = 0, len(self.intervals) - 1
        while start <= end:
            mid = (start + end)//2
            midInterval = self.intervals[mid]
            if midInterval.start == val:
                return
            elif midInterval.start > val:
                end = mid - 1
            else:
                start = mid + 1
        
        # now start is the next insertion index
        index = start

        # get left interval
        if index == 0:
            left_interval = Interval(val, val)
            self.intervals.insert(0, left_interval)
            index += 1
        else:
            left_interval = self.intervals[index-1]

        # a special case to insert val at the end
        if index == len(self.intervals):
            right_interval = Interval(val, val)
            self.intervals.append(right_interval)
        else:
            right_interval = self.intervals[index]
            
        # update the left interval's end
        if val == left_interval.end+1:
            left_interval.end = val

        # update the right interval's start
        if val == right_interval.start-1:
            right_interval.start = val

        # merge left and right intervals, if this is the case
        if left_interval.end == right_interval.start:
            left_interval.end = right_interval.end
            self.intervals.pop(index)
            return

        # left interval and right interval have gap, insert the interval "val"
        if left_interval.end < val and right_interval.start > val:
            self.intervals.insert(index, Interval(val, val))
        

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self.intervals

# 2nd round solution on 5/31/2019
# wrong solution
class SummaryRanges2:
    def __init__(self):
        self.data = []
    
    def addNum(self, val):
        # find the insert position using binary search
        i, j = 0, len(self.data)        
        while i < j:
            mid = (i + j)//2
            if self.data[mid].end < val:
                i = mid + 1
            elif self.data[mid].start > val:
                j = mid
            else:
                return

        # insert new interval at position j
        self.data.insert(j, Interval(val, val))

        # merge interval j-1 and j, we consider only the merge scenario, and ignore the non-merge scenario because inserted interval will remain in j
        if j > 0 and self.data[j-1].end + 1 >= val:
            self.data[j-1].end = max(val, self.data[j-1].end)
            self.data.pop(j)
            j -= 1

        # merge interval j and j+1
        if j + 1 < len(self.data) and val + 1 >= self.data[j+1].start:
            self.data[j].end = self.data[j+1].end
            self.data.pop(j+1)


    def getIntervals(self):
        return self.data

obj = SummaryRanges2()
test_list = [6,6,0,4,8,7,6,4,7,5]
for num in test_list:
    print(num, end = ' -> ')
    obj.addNum(num)
    print(obj.getIntervals())


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()