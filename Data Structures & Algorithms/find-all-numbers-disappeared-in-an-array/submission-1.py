class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        seen = set(nums)
        print(seen)
        disa = []
        for i in range(1,len(nums)+1):
            if i not in seen: 
                disa.append(i)
        return disa

