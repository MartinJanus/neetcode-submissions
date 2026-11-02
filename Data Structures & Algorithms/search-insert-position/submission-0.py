class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        res = len(nums)

        while left <= right:
            half = (left+right)//2
            if nums[half] < target: 
                left = half+1
            elif nums[half] > target:
                res = half
                right = half-1 
            elif nums[half] == target:  
                return half

        return res