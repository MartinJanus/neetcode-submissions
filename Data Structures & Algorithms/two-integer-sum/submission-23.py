class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, v in enumerate(nums):
            required = target - v
            if required in hashmap: 
                answer = [hashmap[required], i]
                return answer
            else:
                hashmap[v] = i