# Method 1 : using two pointers & ord
# version 1
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanS = self.cleanS(s)
        left = 0
        right = len(cleanS) - 1
        while left <= right:
            if cleanS[left] != cleanS[right]:
                return False
            left += 1
            right -= 1
        return True
        
    def cleanS(self, s):
        cleanS = ''
        for char in s:
            if ord('a') <= ord(char) <= ord('z'):
                cleanS += char.lower()
            elif ord('A') <= ord(char) <= ord('Z'):
                cleanS += char.lower()
            elif ord('0') <= ord(char) <= ord('9'):
                cleanS += char.lower()
        return cleanS
#version : 2
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanS = self.clean(s)
        l = 0
        r = len(cleanS) - 1
        while l < r:
            if cleanS[l] != cleanS[r]:
                return False
            l += 1
            r -= 1
        return True

    def clean(self, s):
        cleanS = ''
        for char in s:
            if 65 <= ord(char) <= 90:
                cleanS += char.lower()
            elif 97 <= ord(char) <= 122:
                cleanS += char.lower()
            elif 48 <= ord(char) <= 57:
                cleanS += char
        return cleanS
    
# method 2 : using two pointers and prebuilt function isalnum()
# Version 1
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanS = self.cleanS(s)
        left = 0
        right = len(cleanS) - 1
        while left <= right:
            if cleanS[left] != cleanS[right]:
                return False
            left += 1
            right -= 1
        return True
        
    def cleanS(self, s):
        cleanS = ''
        cleanS = ''.join([char.lower() for char in s if char.isalnum()])
        return cleanS
# version 2
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanS = ''.join([char.lower() for char in s if char.isalnum()])
        left = 0
        right = len(cleanS) - 1
        while left <= right:
            if cleanS[left] != cleanS[right]:
                return False
            left += 1
            right -= 1
        return True

# method 3 : using recursion adn cleaning using ord
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanS = self.cleanS(s)
        left = 0
        right = len(cleanS) - 1
        return self.check(cleanS, left, right)

    def check(self, cleanS, left, right):
        if left >= right:
            return True
        if cleanS[left] != cleanS[right]:
            return False
        else:
            return self.check(cleanS, left+1, right-1)
        
    def cleanS(self, s):
        cleanS = ''
        for char in s:
            if ord('a') <= ord(char) <= ord('z'):
                cleanS += char.lower()
            elif ord('A') <= ord(char) <= ord('Z'):
                cleanS += char.lower()
            elif ord('0') <= ord(char) <= ord('9'):
                cleanS += char.lower()
        return cleanS
    

# 29th April 2024
# practice
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanS = self.clean(s)
        
        l = 0
        r = len(cleanS) - 1
        while l <= r:
            if cleanS[l] != cleanS[r]:
                return False
            l += 1
            r -= 1
        return True

    def clean(self, s):
        cleanS = ''.join(char.lower() for char in s if char.isalnum())
        return cleanS

# solution = Solution()
# print(solution.isPalindrome(s = "A man, a plan, a canal: Panama"))
