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
        # Array per memorizzare i numeri brutti
        ugly_numbers = [0] * n
        ugly_numbers[0] = 1  # Il primo numero brutto è sempre 1
        
        # Indici per i multipli di 2, 3, e 5
        i2 = i3 = i5 = 0
        
        # Valori iniziali di moltiplicatori
        next_multiple_of_2 = 2
        next_multiple_of_3 = 3
        next_multiple_of_5 = 5
        
        for i in range(1, n):
            # Seleziona il prossimo numero brutto più piccolo
            next_ugly = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
            ugly_numbers[i] = next_ugly
            
            # Incrementa gli indici rispettivi e aggiorna i moltiplicatori
            if next_ugly == next_multiple_of_2:
                i2 += 1
                next_multiple_of_2 = ugly_numbers[i2] * 2
            if next_ugly == next_multiple_of_3:
                i3 += 1
                next_multiple_of_3 = ugly_numbers[i3] * 3
            if next_ugly == next_multiple_of_5:
                i5 += 1
                next_multiple_of_5 = ugly_numbers[i5] * 5
        
        return ugly_numbers[-1]
            

if __name__ == "__main__":

    sos = Solution()
    print(sos.nthUglyNumber(144))
    
    
'''
primo prototipo del codice. funziona anche piuttosto bene ma supera i 
limiti temporali di LeetCode e si basa sul brute force
        k = []
        
        for e in range(1, 50000):
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
                if count == 15:
                    break
        return k[n-1]'''
