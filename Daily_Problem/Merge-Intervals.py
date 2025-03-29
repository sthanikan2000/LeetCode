class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]
        # s,e = intervals[0]
        # for interval in intervals[1:]:
        for i in range(1,len(intervals)):
            if intervals[i][0]>res[-1][1]:
                res.append(intervals[i])
            elif intervals[i][1]>res[-1][1]:
                res[-1][1] = intervals[i][1]
        # res.append([s,e])
        return res
        