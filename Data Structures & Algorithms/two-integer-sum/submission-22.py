class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        answer = []

        for i, v in enumerate(nums):
            needed = target - v

            if needed in seen: 
                answer.append(seen[needed])
                answer.append(i)
                return answer
            
            seen[v] = i 
                