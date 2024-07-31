'''
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.

 

Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

Example 2:

Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

 

Constraints:

    1 <= n <= 1690
'''


class Solution:
    def nthUglyNumber(self, n: int) -> int:

        k = []
        
        for e in range(1, 5000):
            count = 0
            j = e
            while e:   
                if e == 1:
                    k.append(e)
                    break
                if e % 2 == 0:
                    e /= 2
                elif e % 3 == 0:
                    e /= 3
                elif e % 5 == 0:
                    e /= 5
                if e == 1:
                    k.append(j)
                    break
                count += 1
                if count == 50:
                    break
        return k[n-1]
            
            

if __name__ == "__main__":

    sos = Solution()
    print(sos.nthUglyNumber(14))