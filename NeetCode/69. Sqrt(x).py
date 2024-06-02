# using a for loop
# version 1
class Solution:
    def mySqrt(self, x: int) -> int:
        prod = 0
        res = 0
        prev = 0
        for i in range(1, x+1):
            prev = i - 1
            res = i
            prod = i * i
            print('prod', prod)
            if prod == x:
                return res
            elif prod < x:
                continue
            if prod > x:
                return prev
        return prev
# version 2:
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        if x == 2:
            return 1
        prod = 0
        res = 0
        prev = 0
        for i in range(1, x):
            prev = i - 1
            res = i
            prod = i * i
            if prod == x:
                return res
            elif prod < x:
                continue
            if prod > x:
                return prev
        return prev
# version 3:
class Solution:
    def mySqrt(self, x: int) -> int:
        prod = 0
        prev = 0
        for i in range(1, x+1):
            prev = i - 1
            prod = i * i
            if prod == x:
                return i
            elif prod < x:
                continue
            if prod > x:
                return prev
        return prev



solution = Solution()
print(solution.mySqrt(x = 9))