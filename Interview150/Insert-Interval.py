class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_int = []
        while intervals and intervals[0][1] < newInterval[0]:
            new_int.append(intervals.pop(0))
        if not intervals:
            new_int.append(newInterval)
            return new_int
        if intervals[0][0] <= newInterval[0]:
            start = intervals[0][0]
        else:
            start = newInterval[0]
        while intervals and newInterval[1]>= intervals[0][1]:
            intervals.pop(0)
        if not intervals:
            new_int.append([start,newInterval[1]])
            return new_int
        if intervals[0][0]<=newInterval[1]:
            new_int.append([start,intervals.pop(0)[1]])
        else:
            new_int.append([start,newInterval[1]])
        while intervals:
            new_int.append(intervals.pop(0))
        return new_int

        

        