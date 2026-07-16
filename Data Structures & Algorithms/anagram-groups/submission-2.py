class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        A = []
        used = set()
        for i in range(len(strs)):
            temp = []
            if i in used:
                continue
            used.add(i)
            for j in range(len(strs)):
                if self.isAnagram(strs[j], strs[i]):
                    temp.append(strs[j])
                    used.add(j)
            A.append(temp)
        return A

    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False