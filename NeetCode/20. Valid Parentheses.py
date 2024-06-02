# using a stack
class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {'(' : ')', '{' : '}', '[' : ']'}
        stack = []
        for char in s:
            if char in hashmap:
                stack.append(hashmap[char])
            else:
                if len(stack) != 0 and char == stack.pop():
                    continue
                else:
                    return False
        return len(stack) == 0
# version 2:
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {'(' : ')', '{' : '}', '[' : ']'}
        for char in s:
            if char in hashmap:
                stack.append(hashmap[char])
            else:
                if len(stack) == 0 or char != stack.pop():
                    return False
        return len(stack) == 0
    

    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in '([{':
                stack.append( {'(':')', '[':']', '{':'})' }[char] )
            elif not stack or stack.pop() != char:
                return False
        return not stack
        

def getPrimeNumbers(arr):
    prime_numbers = []
    for num in arr:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
