class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        calculate = float('inf')
        total = 0

        while right < len(nums):
            total += nums[right]
            right += 1

            while total >= target:
                calculate = min(calculate, right - left)
                total -= nums[left]
                left += 1

        return calculate if calculate != float('inf') else 0
