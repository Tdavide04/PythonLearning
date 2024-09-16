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
        timePointsMins: list = []  # List to store the converted time points in minutes
        minDiff = float("inf")  # Initialize minDiff to infinity, to find the minimum difference later
        
        # Convert each time point (HH:MM) into minutes and store in timePointsMins
        for num in timePoints:
            # Convert the time from "HH:MM" to minutes: HH*60 + MM
            timePointsMins.append(int(num[3:]) + (int(num[:2]) * 60))
        
        # Sort the list of time points in minutes
        timePointsMins.sort()
        
        # Find the minimum difference between consecutive time points
        for i in range(1, len(timePointsMins)):
            minDiff = min(minDiff, timePointsMins[i] - timePointsMins[i-1])
        
        # Account for the time difference across midnight (circular comparison)
        minDiff = min(minDiff, (24*60 - timePointsMins[-1] + timePointsMins[0]))
        
        return minDiff  # Return the minimum time difference




if __name__ == "__main__":

    sos = Solution()
    print(sos.findMinDifference(["00:00","12:00","23:59"]))