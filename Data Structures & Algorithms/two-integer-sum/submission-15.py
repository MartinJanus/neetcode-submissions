class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #inputs an array of ints, a target int
        #need to check against every index if it adds up to the target
        #brute force would involve 2 for loops checking each index, if it equals target return the indexs. 
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    output = [i,j]
                    return output
                else:
                    continue
