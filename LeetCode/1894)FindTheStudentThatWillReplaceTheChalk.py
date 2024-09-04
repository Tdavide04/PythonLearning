'''
There are n students in a class numbered from 0 to n - 1. The teacher will give each student a problem starting with the student number 0, then the student number 1, and so on until the teacher reaches the student number n - 1. After that, the teacher will restart the process, starting with the student number 0 again.

You are given a 0-indexed integer array chalk and an integer k. There are initially k pieces of chalk. When the student number i is given a problem to solve, they will use chalk[i] pieces of chalk to solve that problem. However, if the current number of chalk pieces is strictly less than chalk[i], then the student number i will be asked to replace the chalk.

Return the index of the student that will replace the chalk pieces.

 

Example 1:

Input: chalk = [5,1,5], k = 22
Output: 0
Explanation: The students go in turns as follows:
- Student number 0 uses 5 chalk, so k = 17.
- Student number 1 uses 1 chalk, so k = 16.
- Student number 2 uses 5 chalk, so k = 11.
- Student number 0 uses 5 chalk, so k = 6.
- Student number 1 uses 1 chalk, so k = 5.
- Student number 2 uses 5 chalk, so k = 0.
Student number 0 does not have enough chalk, so they will have to replace it.

Example 2:

Input: chalk = [3,4,1,2], k = 25
Output: 1
Explanation: The students go in turns as follows:
- Student number 0 uses 3 chalk so k = 22.
- Student number 1 uses 4 chalk so k = 18.
- Student number 2 uses 1 chalk so k = 17.
- Student number 3 uses 2 chalk so k = 15.
- Student number 0 uses 3 chalk so k = 12.
- Student number 1 uses 4 chalk so k = 8.
- Student number 2 uses 1 chalk so k = 7.
- Student number 3 uses 2 chalk so k = 5.
- Student number 0 uses 3 chalk so k = 2.
Student number 1 does not have enough chalk, so they will have to replace it.

 

Constraints:

    chalk.length == n
    1 <= n <= 105
    1 <= chalk[i] <= 105
    1 <= k <= 109
'''

class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        # Initialize index to start from the first student
        i = 0
        # Calculate the total sum of chalk needed by all students
        summ = sum(chalk)
        # Reduce k modulo the total sum of chalk to handle large k values efficiently
        while summ < k:
            k %= summ
        # Loop to determine which student will run out of chalk
        while True:
            # If the index exceeds the number of students, reset it to the first student
            if i > len(chalk) - 1:
                i -= len(chalk)
            # Subtract the current student's chalk usage from k
            k -= chalk[i]
            # If k becomes negative, the current student is the one who will run out of chalk
            if k < 0:
                return i 
            # Move to the next student
            i += 1



if __name__ == "__main__":

    sos = Solution()
    print(sos.chalkReplacer(chalk = [3,4,1,2], k = 25))
    print(sos.chalkReplacer(chalk = [5,1,5], k = 22))
    print(sos.chalkReplacer(chalk = [100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1], k = 500000))
    print(sos.chalkReplacer(chalk = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], k = 1000000000))
    print(sos.chalkReplacer(chalk = [7, 7, 3, 9, 2], k = 14))
    print(sos.chalkReplacer(chalk = [1], k = 1000000000))
    print(sos.chalkReplacer(chalk = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], k = 10))
    print(sos.chalkReplacer(chalk = [1,2,3,4,5,6,7,8,9], k = 45))
