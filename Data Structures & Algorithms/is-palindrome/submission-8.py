class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaNum = []
        for c in s: 
            if c.isalnum():
                alphaNum.append(c.lower())

        left = 0
        right = len(alphaNum)-1

        while left < right: 
            if alphaNum[left] == alphaNum[right]:
                left+=1
                right-=1
            else:
                return False

        return True
        


