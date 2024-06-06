# Approach 1
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        n = bin(n)
        for char in n:
            if char == '1':
                res += 1
        return res
    

# Approach 2 # using and operation and right shift
class Solution:
    def hammingWeight(self, n: int) -> int:
        num = bin(n)[2:]
        num = int(num)
        res = 0
        print('num', num)
        while num:
            digit = num & 1
            print('digit', digit)
            res += digit
            num >>= 1
            print('num', num)
        return res
    
# Approach 3: using bit manipulation
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            digit = n % 2
            print('digit', digit)
            res += digit
            n //= 2
            print('n', n)
        return res
    
solution = Solution()
print(solution.hammingWeight(11))