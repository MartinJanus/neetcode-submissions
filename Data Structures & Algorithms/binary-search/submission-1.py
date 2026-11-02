class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # for i in range(len(nums)):
        #     if(nums[i]==target):
        #         return i
            
        # return -1

        left=0
        right=len(nums)-1

        while left <= right:
            half = (left+right)//2
            if nums[half] < target: 
                left = half+1
            elif nums[half] > target:
                right = half-1 
            else:  
                return half
        return -1
                
