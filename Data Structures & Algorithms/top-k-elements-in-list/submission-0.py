class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first we count frequency of nums
        nums_count = {}
        result = []

        for i in nums: 
            nums_count[i] = nums_count.get(i,0)+1

        ordered_numbers = sorted(
            nums_count,
            key=nums_count.get,
            reverse=True
        )

        print(ordered_numbers)
        result = ordered_numbers[:k]
        return(result)