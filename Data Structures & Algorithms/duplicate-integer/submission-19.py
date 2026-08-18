class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # input is an array with 4 numbers 
        # must check each number in the array and determine if there is more than 1 of the same value
        # Easy solution is to check with a set(), can't have duplicate values. Otherwise can iterate with 2 for loops brute force, check integer A against the rest of the array and iterate. 
        # output is a boolean 
        seen = set()
        for num in nums: 
            if num in seen: 
                return True 
            seen.add(num)
        return False
        
        #Time complexity: O(n^2) because we have a set which adds which is O(n), then we have for loop and if statement in so it is O(n^2)
