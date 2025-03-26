class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def timeDiff(x,y):
            if x<=y:
                return int(y[:2])*60+int(y[-2:])-int(x[:2])*60-int(x[-2:])
            return -int(x[:2])*60-int(x[-2:])+(24+int(y[:2]))*60+int(y[-2:])

        timePoints.sort()
        minTime = timeDiff(timePoints[-1],timePoints[0])
        for i in range(len(timePoints)):
            x = timeDiff(timePoints[i-1],timePoints[i])
            if x == 0:
                return 0
            elif x<minTime:
                minTime=x
        return minTime
        
