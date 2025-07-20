'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
'''

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        
        if n == 0: # If n is 0, no need to plant any flowers, so return True
            return True
        
        for e in range(len(flowerbed)):
            if len(flowerbed) == 1: # Special case: if flowerbed has only one plot
                if flowerbed[e] == 0: # Check if the only plot is empty
                    flowerbed[e] = 1 # Plant a flower in this plot
                    n -= 1 # Decrease the number of flowers to be planted
                    
            elif e == 0: # Special case: first plot in the flowerbed
                 if flowerbed[e] == 0 and flowerbed[e + 1] == 0: # Check if the first plot and the next plot are both empty
                    flowerbed[e] = 1 # Plant a flower in the first plot
                    n -= 1 # Decrease the number of flowers to be planted
                    
            elif e == len(flowerbed) -1: # Special case: last plot in the flowerbed
                if flowerbed[e] == 0 and flowerbed[e - 1] == 0: # Check if the last plot and the previous plot are both empty
                    flowerbed[e] = 1 # Plant a flower in the last plot
                    n -= 1 # Decrease the number of flowers to be planted
                    
            else: # General case: plots in the middle of the flowerbed
                if flowerbed[e - 1] == 0: # Check if the previous plot is empty
                    if flowerbed[e] == 0: # Check if the current plot is empty
                        if flowerbed[e + 1] == 0: # Check if the next plot is empty
                            flowerbed[e] = 1 # Plant a flower in the current plot
                            n -= 1 # Decrease the number of flowers to be planted
                            
            if n == 0: # If we have successfully planted all required flowers, return True
                return True
        return False


if __name__ == "__main__":
    
    sos = Solution()
    print(sos.canPlaceFlowers(flowerbed = [1,0,0,0,1,0,0], n = 2))