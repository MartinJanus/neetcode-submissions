class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        #sorted in ascending order. 
        #

        left = 0 
        right = len(numbers) - 1
        answer = []

        while left < right: 
            s = numbers[left] + numbers[right]
            if s < target:
                left+=1
            elif s > target: 
                right-=1
            else: 
                answer.append(left+1)
                answer.append(right+1)
                return answer
        
        return answer