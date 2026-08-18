class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #inputs: two strings 
        #brute force solution is to sort both strings, compare each string. if they match then return True, otherwise false. 
        #more optimal solution - check each letter frequency, if they are the same then the words are the same - using a dictionary. 
        if sorted(s) == sorted(t): #O(N)  O(nlogn)
            return True
        else:
            return False