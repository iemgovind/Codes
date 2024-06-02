# Method 1 : Brute Force
# Using two For Loops
# Gives TLE on Leetcode
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
    

# Method 2 : Using Hashmap
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                return True
            else:
                hashmap[num] = num
        return False
    
# Method 3 : Using a predefined function SET()
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
    

# Method 4 : Sorting the list
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
    
# Method 5: Using prebuild function count
# Will give TLE
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for num in nums:
            if nums.count(num) > 1:
                return True
        return False
    
# Method 6 : Using prebuilt function Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = Counter(nums)
        for key in hashmap:
            if hashmap[key] != 1:
                return True
        return False

# 29 Apr 2024
# Practice : 
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setOfNums = set(nums)
        sumOfNums = 0
        sumOfSetOfNums = 0
        for num in nums:
            sumOfNums += num
        for num in setOfNums:
            sumOfSetOfNums += num
        print('sumOfNums', sumOfNums)
        print('sumOfSetOfNums', sumOfSetOfNums)
        return sumOfSetOfNums == setOfNums
    
solution = Solution()
# print(solution.containsDuplicate(nums = [1,2,3,4]))
print(solution.containsDuplicate(nums = [1,2,3,1]))
