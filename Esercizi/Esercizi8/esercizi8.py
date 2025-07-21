#Esercitazione su Classi e Funzioni

#Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).
#Implement the MyStack class:
#- push(x: int) -> None: Pushes element x to the top of the stack.
#- pop() -> None Removes the element on the top of the stack and returns it.
#- pop() -> None Returns the element on the top of the stack.
#- empty() -> None Returns true if the stack is empty, false otherwise.

class Queue:
    pass

class MyStack:
    def __init__(self):
        self.lista = []

    def push(self, x: int) -> None:
        self.lista.append(x)

    def top(self):
        if not self.lista:
            return None
        return self.lista[-1]

    def pop(self):
        if not self.lista:
            return None
        return self.lista.pop()

    def empty(self):
        if self.lista:
            return False
        return True
	

#Given a string s which consists of lowercase or uppercase letters, 
#write a function that returns the length of the longest palindrome that can be built with those letters. 
#Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
#Example: print(longest_palindrome("abccccdd"))
# -> 7

def longest_palindrome(s: str) -> int:
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    count = 0
    odd_count = 0
    for char in freq:
        if freq[char] % 2 == 0:
            count += freq[char]
        else:
            count += freq[char] - 1
            odd_count += 1

    return count + (1 if odd_count > 0 else 0)

#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', write a function to determine if the input string is valid.
#An input string is valid if: 
#    Open brackets must be closed by the same type of brackets.
#    Open brackets must be closed in the correct order.
#    Every close bracket has a corresponding open bracket of the same type.

#print(is_valid_parenthesis("()"))
# -> True

def is_valid_parenthesis(s: str) -> bool:
    stack = []    
    for char in s:
        if char in '({[':
            stack.append(char)
        else:
            if not stack:
                return False
            top_element = stack.pop()
            if char == ')' and top_element != '(':
                return False
            if char == '}' and top_element != '{':
                return False
            if char == ']' and top_element != '[':
                return False
    return not stack
   
    
#You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
#representing the number of elements in nums1 and nums2 respectively. Write a function to merge nums1 and nums2 into a single array sorted in non-decreasing order.
#The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
#To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
#and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
#nums1 = [1, 2, 3, 0, 0, 0]
#m = 3
#nums2 = [2, 5, 6]
#n = 3
#merge(nums1, m, nums2, n)
#print(nums1)  
# -> [1, 2, 2, 3, 5, 6]

def merge(nums1, m, nums2, n):
    for _ in range(n):
        nums1.pop(-1)
    for i in range(n):
        nums1.append(nums2[i])
    return nums1.sort()
    
#Given the head of a singly linked list, return true if it is a palindrome. Model the Node and Linked List concepts using classes. 

'''
class LinkedList:
    def __init__(self):
        lista = []
        
def is_palindrome(head: Node) -> list[int]:
    lista1 = LinkedList.lista.reverse()
    if LinkedList.lista == lista1:
        return True
    else:
        return False

 	
ll1 = LinkedList()
for value in [1, 2, 3, 2, 1]:
    ll1.append(value)
print(is_palindrome(ll1.head))
'''

#Exercise 1: Creating an Abstract Class with Abstract Methods
#Create an abstract class Shape with an abstract method area and another abstract method perimeter. 
#Then, create two subclasses Circle and Rectangle that implement the area and perimeter methods.

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
class Circle(Shape):
    
    def __init__(self, radius: float):
        self.radius = radius
        
    def area(self):
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
class Rectangle(Shape):
    
    def __init__(self, length: float, width: float):
       self.length = length
       self.width = width
       
    def area(self):
        return self.width * self.length
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
#Exercise 2: Implementing Static Methods
# Create a class MathOperations with a static method add that takes two numbers and returns their sum, 
# and another static method multiply that takes two numbers and returns their product.

class MathOperations:
    
    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b
    
    @staticmethod
    def add(a, b):       
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
