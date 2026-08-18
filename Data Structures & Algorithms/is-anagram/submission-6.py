class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #inputs: two strings 
        #brute force solution is to sort both strings, compare each string. if they match then return True, otherwise false. 
        #more optimal solution - check each letter frequency, if they are the same then the words are the same - using a dictionary. 
        # if sorted(s) == sorted(t): #O(N)  O(nlogn)
        #     return True
        # else:
        #     return False
        # dictionary solution
        # word = [s, t]
        # print(word)
        # counts = [0] * 26
        # for i in range(len(word)):
        #     print(word[i])
        #     for char in word[i]:
        #         print(char)
        #         index = ord(char) - ord("a")
        #         print(index)
        #         counts[index]+=1
        #     # counts[char] = counts.get(char,0) + 1 
        #         print(counts)   
        if len(s) != len(t):
            return False 
        
        count_s = {}
        count_t = {}

        for char in s: 
            count_s[char] = count_s.get(char,0)+1
        
        for char in t: 
            count_t[char] = count_t.get(char,0)+1

        if count_s == count_t:
            return True
        else:
            return False