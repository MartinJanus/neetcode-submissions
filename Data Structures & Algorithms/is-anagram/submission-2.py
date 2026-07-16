class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #should sort, then compare
        if sorted(s) == sorted(t):
            return True
        else:
            return False
        