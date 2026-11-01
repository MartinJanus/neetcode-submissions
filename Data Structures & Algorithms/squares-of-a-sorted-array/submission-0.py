class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = []
        for i in nums: 
            res = i*i
            # print(res)
            arr.append(res)
    
        return sorted(arr)