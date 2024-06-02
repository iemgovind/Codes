from collections import Counter
s = "anagram"
t = "nagaram"
print(Counter(s))
print(Counter(t))
print(Counter(s) == Counter(t))
s_counter = Counter(s)
t_counter = Counter(t)

result = True
for key in s_counter:
    if key not in t_counter or s_counter[key] != t_counter[key]:
        result = False
        break
for key in t_counter:
    if key not in s_counter or t_counter[key] != s_counter[key]:
        result = False
        break
print(result)

# Method 1 : Using defaultdict(int) i.e a hashmap to count the no of ocurring 
# alphabets
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        myMap = defaultdict(int)
        for i in range(len(s)):
            myMap[s[i]] += 1
            myMap[t[i]] -= 1
        for val in myMap.values():
            if val != 0:
                return False
        return True
    
# Method 2 : using two hashmap
# Version 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap_s = {}
        hashmap_t = {}
        for i in range(len(s)):
            if s[i] in hashmap_s:
                hashmap_s[s[i]] += 1
            else:
                hashmap_s[s[i]] = 1
            if t[i] in hashmap_t:
                hashmap_t[t[i]] += 1
            else:
                hashmap_t[t[i]] = 1
        return hashmap_s == hashmap_t
# Version 2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap_s = {}
        hashmap_t = {}
        for i in range(len(s)):
            if s[i] in hashmap_s:
                hashmap_s[s[i]] += 1
            else:
                hashmap_s[s[i]] = 1
            if t[i] in hashmap_t:
                hashmap_t[t[i]] += 1
            else:
                hashmap_t[t[i]] = 1
        for key in hashmap_s:
            if hashmap_s.get(key) != hashmap_t.get(key):
                return False
        return True
    

# Method 3 : using pre-build function Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    

# Method 4 : using fixed length array : using ord 
# Version 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        myList_s = [0] * 26
        myList_t = [0] * 26
        for i in range(len(s)):
            indexS = self.giveIndex(s[i])
            myList_s[indexS] += 1
            indexT = self.giveIndex(t[i])
            myList_t[indexT] += 1
        return myList_s == myList_t

    def giveIndex(self, char):
        return ord(char) - ord('a')
# Version 2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        myList = [0] * 26
        for i in range(len(s)):
            indexS = self.giveIndex(s[i])
            myList[indexS] += 1
            indexT = self.giveIndex(t[i])
            myList[indexT] -= 1
        return myList == [0] * 26

    def giveIndex(self, char):
        return ord(char) - ord('a')
# Version 3
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        myList = [0] * 26
        for i in range(len(s)):
            myList[ord(s[i]) - ord('a')] += 1
            myList[ord(t[i]) - ord('a')] -= 1
        return myList == [0] * 26
# Version 4 # using 26 alphabet and ord
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        myList = [0] * 26
        for i in range(len(s)):
            myList[ord(s[i]) - ord('a')] += 1
            myList[ord(t[i]) - ord('a')] -= 1
        for val in myList:
            if val != 0:
                return False
        return True
    

# Method 5 : Sorting
# Version 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True
# Version 2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
    
# 29 apr 2024
# practice
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        array = [0] * 26
        for i in range(len(s)):
            index = self.getIndex(s[i])
            array[index] += 1
            index = self.getIndex(t[i])
            array[index] -= 1
        for num in array:
            if num != 0:
                return False
        return True
    
    def getIndex(self, i):
        return ord(i) - ord('a')
