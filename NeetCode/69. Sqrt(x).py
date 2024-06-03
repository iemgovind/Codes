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
# version 4:
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        for i in range(x+1):
            prod = i * i
            if prod > x:
                return i-1
        return -1
    
# Approach 2: using binary search
class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        while l <= r:
            mid = l + ((r - l) // 2)
            prod = mid * mid
            if prod < x:
                l = mid + 1
            elif prod > x:
                r = mid -1
            else:
                return mid
        return r
		# When there is no perfect square, 'r' is the the value on the left
        # of where it would have been (rounding down). If we were rounding up, 
        # we would return 'l'
        # When the loop exits, right will be the largest integer such that 
        # right * right is less than or equal to x. Therefore, return right.



solution = Solution()
print(solution.mySqrt(x = 9))