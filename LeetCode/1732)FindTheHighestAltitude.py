'''
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

 

Example 1:

Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
Example 2:

Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.
 

Constraints:

n == gain.length
1 <= n <= 100
-100 <= gain[i] <= 100
'''

class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        max_altitude: int = float('-inf') # Initialize max_altitude to negative infinity to ensure any altitude will be higher.
        curr_altitude: int = 0 # Initialize curr_altitude to 0, as the starting altitude is considered to be 0.
        for num in gain:
            curr_altitude += num 
            # Update max_altitude to the highest value between the current altitude,
            # the current max_altitude, and 0 (to ensure it never goes below 0).
            max_altitude = max(max_altitude, curr_altitude, 0)
        return max_altitude
        
        
if __name__ == "__main__":
    
    sos = Solution()
    print(sos.largestAltitude(gain = [-5,1,5,0,-7]))