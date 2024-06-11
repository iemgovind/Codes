# Approach 1: using two for loops
# TC : O(n^2)    SC: O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return -1

# Approach 2: using two pointers
# Tc : O(n)   SC : O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            toFind = target - nums[i]
            if toFind in hashmap:
                return [hashmap[toFind], i]
            else:
                hashmap[nums[i]] = i
        return -1