# Approach 1: Using a hashmap
class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        hashmap = {}
        hashmap[n] = 1
        num = 0
        while True:
            n = self.sumOfSquares(n)
            print('num', num)
            if n == 1:
                return True
            if n in hashmap:
                break
            else:
                hashmap[n] = 1
            print('hashmap', hashmap)
        return False
        
    def sumOfSquares(self, n):
        res = 0
        while n:
            digit = n % 10
            res += digit * digit
            n //= 10
        return res
    
# Approach 2 : using slow and fast pointers
class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        slow = n
        fast = n
        while True:
            slow = self.sumOfSquares(slow)
            fast = self.sumOfSquares(self.sumOfSquares(fast))
            if slow == 1:
                return True
            if slow == fast:
                break
        return slow == 1
        
    def sumOfSquares(self, n):
        res = 0
        while n:
            digit = n % 10
            res += digit * digit
            n //= 10
        return res

    
solution = Solution()
print(solution.isHappy(n = 19))