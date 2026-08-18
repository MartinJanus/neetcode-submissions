class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #inputs: two strings 
        #brute force solution is to sort both strings, compare each string. if they match then return True, otherwise false. 
        #more optimal solution - check each letter frequency, if they are the same then the words are the same - using a dictionary. 
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        if sorted_s == sorted_t:
            return True
        else:
            return False