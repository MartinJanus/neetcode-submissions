class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #inputs an array of ints, a target int
        #need to check against every index if it adds up to the target
        #brute force would involve 2 for loops checking each index, if it equals target return the indexs. 
        # for i in range(len(nums)): # o(n)
        #     for j in range(len(nums)): # o(n)
        #         if nums[i] + nums[j] == target and i != j: #o(1)
        #             output = [i,j]
        #             return output
        #         else:
        #             continue
        #I think can be done with a dictionary
        seen = {}

        #enumerate gives us both index and number
        for i, number in enumerate(nums):

            #calculate the number to reach the target
            needed = target - number
            # see if its in our dictionary
            if needed in seen: 
                # Return the needed number's previous index
                # and the current number's index.
                return [seen[needed], i]
                
            #store current number and index
            seen[number] = i


