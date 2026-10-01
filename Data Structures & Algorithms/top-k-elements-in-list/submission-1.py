class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first we count frequency of nums
        nums_count = {}

        # counting frequency of numbers occurring. 
        for i in nums: 
            nums_count[i] = nums_count.get(i,0)+1

        # sorting numbers by their frequency, from highest to lowest. 
        ordered_numbers = sorted(
            nums_count,
            key=nums_count.get,
            reverse=True
        )

        print(ordered_numbers)
        #slicing the result to only return the first K numbers. 
        result = ordered_numbers[:k] 
        return(result)