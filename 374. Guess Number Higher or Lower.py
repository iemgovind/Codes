# Aprroach 1 : using a for loop will give TLE

# TC : O( \n) SC : O(1)   
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        for i in range(1, n+1):
            num = guess(i)
            if num == 0:
                return i
        return -1

# approach 2: using a binary search 
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        while True:
            mid = l + ((r - l) // 2)
            num = guess(mid)
            if num < 0:
                r = mid - 1
            elif num > 0:
                l = mid + 1
            else:
                return mid
        return -1