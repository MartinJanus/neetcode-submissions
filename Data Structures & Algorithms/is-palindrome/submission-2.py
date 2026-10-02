class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted = ""
        for c in s:
            if c.isalnum(): # looping through each character in string, and checking if its alphanumeric (a-z)(0-9)
                formatted+=c.lower() #adding to formatted string, only alphanumeric and all lower case 

        reversed_string = formatted[::-1] #reversing string, slice that steps backwards -1

        return reversed_string == formatted