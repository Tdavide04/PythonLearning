'''
You have observations of n + m 6-sided dice rolls with each face numbered from 1 to 6. n of the observations went missing, and you only have the observations of m rolls. Fortunately, you have also calculated the average value of the n + m rolls.

You are given an integer array rolls of length m where rolls[i] is the value of the ith observation. You are also given the two integers mean and n.

Return an array of length n containing the missing observations such that the average value of the n + m rolls is exactly mean. If there are multiple valid answers, return any of them. If no such array exists, return an empty array.

The average value of a set of k numbers is the sum of the numbers divided by k.

Note that mean is an integer, so the sum of the n + m rolls should be divisible by n + m.

 

Example 1:

Input: rolls = [3,2,4,3], mean = 4, n = 2
Output: [6,6]
Explanation: The mean of all n + m rolls is (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4.
Example 2:

Input: rolls = [1,5,6], mean = 3, n = 4
Output: [2,3,2,2]
Explanation: The mean of all n + m rolls is (1 + 5 + 6 + 2 + 3 + 2 + 2) / 7 = 3.
Example 3:

Input: rolls = [1,2,3,4], mean = 6, n = 4
Output: []
Explanation: It is impossible for the mean to be 6 no matter what the 4 missing rolls are.
 

Constraints:

m == rolls.length
1 <= n, m <= 105
1 <= rolls[i], mean <= 6
'''

class Solution:
    def missingRolls(self, rolls: list[int], mean: int, n: int) -> list[int]:
        '''
        total rolls / m + n = mean =>
        rolls + x / m + n = mean =>
        rolls + x = mean * (m + n) =>
        x = [mean * (m + n)] - rolls
        x = incognita
        mean = operation result 
        m = len(rolls)
        n = observations went missing
        '''
        m: int = len(rolls)
        x = mean*(m+n) - sum(rolls)
        if x < n or x > 6 * n:
            return []
        result = [x // n] * n
        resto = x % n
        for i in range(resto):
            result[i] += 1
        return result

        
            
    
if __name__ == "__main__":
    
    sos = Solution()
    print(sos.missingRolls(rolls = [3,2,4,3], mean = 4, n = 2))
    print(sos.missingRolls([3,2,4,3], 5, 54356))
    print(sos.missingRolls([1,5,6], 2, 36575))
    print(sos.missingRolls([6,3,4,3,5,3], 1, 6))
    print(sos.missingRolls([4,2,2,5,4,5,4,5,3,3,6,1,2,4,2,1,6,5,4,2,3,4,2,3,3,5,4,1,4,4,5,3,6,1,5,2,3,3,6,1,6,4,1,3], 2, 53))
    print(sos.missingRolls([1, 3, 5, 2, 6, 4, 3, 2, 5, 1, 6, 4, 2, 3, 5, 1, 4, 6, 2, 5, 3, 6, 1, 4, 5], 4, 100000))
    print(sos.missingRolls([3, 5, 1, 6, 4, 2, 2, 6, 4, 3, 5, 1, 6, 2, 4, 1, 6, 5, 3, 2, 4, 6, 1, 5, 3, 4, 2, 6, 1, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 5, 2, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6, 1, 2, 5, 3, 4, 6], 3, 100000))
    print(sos.missingRolls([6, 6, 6, 6], 6, 1))
    print(sos.missingRolls([1, 1, 1, 1], 6, 1))
    print(sos.missingRolls([6,3,4,3,5,3], 1, 6))
    print(sos.missingRolls([4,2,2,5,4,5,4,5,3,3,6,1,2,4,2,1,6,5,4,2,3,4,2,3,3,5,4,1,4,4,5,3,6,1,5,2,3,3,6,1,6,4,1,3], 2, 53))
    
    

