class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted = ""
        for c in s:
            if c.isalnum():
                formatted+=c.lower()

        reversed_string = formatted[::-1]

        return reversed_string == formatted