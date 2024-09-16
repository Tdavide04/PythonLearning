'''
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.

 

Example 1:

Input: timePoints = ["23:59","00:00"]
Output: 1

Example 2:

Input: timePoints = ["00:00","23:59","00:00"]
Output: 0

 

Constraints:

    2 <= timePoints.length <= 2 * 104
    timePoints[i] is in the format "HH:MM".
'''

class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        timePointsMins: list = []
        minDiff = float("inf")
        for num in timePoints:
            timePointsMins.append(int(num[3:])+(int(num[:2])*60))
        for i in range(len(timePointsMins)-1):
            for j in range(i+1, len(timePointsMins)):
                curr = abs(timePointsMins[i] - timePointsMins[j])
                if curr < minDiff:
                    minDiff = curr
        return minDiff



if __name__ == "__main__":

    sos = Solution()
    print(sos.findMinDifference(["00:00","23:59","00:00"]))