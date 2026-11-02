class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        nums.sort()
        for i in range(len(nums)):

            left = i+1
            right = len(nums)-1

            while left < right: 

                target = -(nums[left] + nums[right])
                
                if nums[i] == target: 
                    answer.add((nums[left], nums[right], nums[i]))
                    left+=1
                    right-=1
                elif nums[i] < target: 
                    left+=1
                else: 
                    right-=1

        return list(answer)