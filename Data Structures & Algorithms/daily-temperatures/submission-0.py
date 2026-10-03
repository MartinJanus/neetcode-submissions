class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        result = [0]*len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp: 
                previousIndex = stack.pop()
                result[previousIndex] = i - previousIndex
            stack.append(i)
    
        return result

