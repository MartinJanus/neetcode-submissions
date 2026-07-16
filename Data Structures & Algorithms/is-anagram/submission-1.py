class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #should sort, then compare
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        if sorted_s == sorted_t:
            return True
        else:
            return False
        