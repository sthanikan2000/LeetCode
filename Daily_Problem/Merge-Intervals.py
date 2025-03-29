class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = []
        s,e = intervals[0]
        for interval in intervals[1:]:
            if interval[0]>e:
                res.append([s,e])
                s,e = interval
            elif interval[1]>e:
                e = interval[1]
        res.append([s,e])
        return res
        