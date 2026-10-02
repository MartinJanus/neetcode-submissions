class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
                # prefix and postfix solution 
        # prefix: 1 
        # nums = [1,2,4,6]
        # 1*1 = nums [1,] - prefix value goes into array

        # prefix: 1
        # 1 * 2 = [1,1]

        # prefix: 2: 
        # 2 * 4 = 8  = [1,1,2,]

        # prefix = 8:
        # 4 * 6 = 24 = [1,1,2,8]

        # prefix = 24:

        # reverse: 
        # postfix = 1
        # [1,1,2,8]

        # postfix = 1 [1,2,4,6]

        # 6*1 = 6 
        # [1,1,12,8]

        # postfix = 6*4 = 24 
    
        # [1,24,12,8]
        # 24 * 2 
        # [48,24,12,8]
        # 48 * 1 
        prefix = 1
        postfix = 1
        result = []

        for i in range(len(nums)): 
            result.append(prefix)
            prefix*=nums[i]

        for i in range(len(nums)-1,-1,-1):
            result[i]*=postfix
            postfix*=nums[i]


        return result


        

