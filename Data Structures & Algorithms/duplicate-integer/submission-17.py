class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # compare first value to all other values, then compare second value to all other values, then 3rd
        seen = set()
        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i)
        return False;