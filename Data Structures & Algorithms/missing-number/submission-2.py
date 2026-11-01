class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        counter = 0
        for i in range(len(nums)):
            nums.sort()
            if counter != nums[i]: 
                return counter
            else:
                counter+=1
        return counter
        