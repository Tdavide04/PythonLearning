'''
You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

You are also given an integer k, which is the desired number of consecutive black blocks.

In one operation, you can recolor a white block such that it becomes a black block.

Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

 

Example 1:

Input: blocks = "WBBWWBBWBW", k = 7
Output: 3
Explanation:
One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
so that blocks = "BBBBBBBWBW". 
It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
Therefore, we return 3.
Example 2:

Input: blocks = "WBWBBBW", k = 2
Output: 0
Explanation:
No changes need to be made, since 2 consecutive black blocks already exist.
Therefore, we return 0.
 

Constraints:

n == blocks.length
1 <= n <= 100
blocks[i] is either 'W' or 'B'.
1 <= k <= n
'''

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = 0 # Initialize a counter for the number of 'W' in the current window
        min_change = len(blocks)
        for i in range(len(blocks)):
            # Define the left and right boundaries of the current window
            left_point = i
            left_point = i
            right_point = i + k
            if right_point > len(blocks): # If the right boundary exceeds the string length, break the loop
                break
            for e in blocks[left_point:right_point]: # Iterate through the characters in the current window
                if e == "W": # Increment the count if the character is 'W'
                    count += 1
            if count < min_change: # If the current window requires fewer changes than the previously recorded minimum, update it
                min_change = count
            count = 0 # Reset the count for the next iteration
        return min_change
                    
        
    
    
if __name__ == "__main__":
    
    sos = Solution()
    print(sos.minimumRecolors(blocks = "WBBWWWWBBWWBBBBWWBBWWBBBWWBBBWWWBWBWW", k = 15))
    
    
# Personal notes:    
# Creo una finestra lunga k e scorro la lista
# Creo una variabile min_change uguale a len(stringa)
# Analizzo la somma e di bianchi e neri, il numero dei bianchi è uguale a min_change
# Piano piano che vado avanti min_change cambierà nel caso ci siano meno W rispetto a prima 
# Dopo aver finito tutta la lista return min_change