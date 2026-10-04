class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #need the largest width, multiplied by the smallest of the two heights to form the total area.

        l = 0 
        r = len(heights)-1 
        result = 0


        while l < r: 
            maxArea = abs((l - r) * min(heights[l], heights[r]))
            result = max(result, maxArea)
            if (heights[l] < heights[r]):
                l+=1
            else:
                r-=1
        
        return(result)
            
            


