class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # can use a dictionary of frequency of letters
        # compare s and t, if they are the same frequency, they are anagrams 

        if len(t) != len(s):
            return False

        s_count = {}
        t_count = {}


        for char in s: 
            s_count[char] = s_count.get(char, 0)+1
        
        for char in t: 
            t_count[char] = t_count.get(char, 0)+1

        return t_count == s_count