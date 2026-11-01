class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0 
        right = len(nums)-1
        result = []

        while left != right:
            if abs(nums[right]) > abs(nums[left]):
                result.append(nums[right]**2)
                right-=1
            else: 
                result.append(nums[left]**2)
                left+=1
            
        result.append(nums[left]**2)
        

        return result[::-1]