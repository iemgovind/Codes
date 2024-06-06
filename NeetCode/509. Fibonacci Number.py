# Approach 1: using recursion 
# TC : O(n^2)  SC : O(n)

class Solution:
    def fib(self, n: int) -> int:
        def fibonacci(n):
            if n < 2:
                return n
            else:
                return fibonacci(n-1) + fibonacci(n-2)
                
        return fibonacci(n)

# Approach 2: using a for loop:
# TC : O(n)  SC : O(n)

class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        array = [0] * (n+1)
        array[0] = 0
        array[1] = 1
        for i in range(2, n+1):
            array[i] = array[i-1] + array[i-2]
        return array[n]
    
# Version 2:
# TC : O(n)    SC : O(1)
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        num1 = 0
        num2 = 1
        res = 0
        for i in range(2, n+1):
            res = num1 + num2
            num1 = num2
            num2 = res
        return res