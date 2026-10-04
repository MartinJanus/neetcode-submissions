class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #need the largest width, multiplied by the smallest of the two heights to form the total area.

        l = 0 
        r = len(heights)-1 

        # maximum = []
        result = 0


        while l < r: 
            height = min(heights[l], heights[r])
            width = l - r
            maxArea = abs(width*height)
            result = max(result, maxArea)
            if (heights[l] < heights[r]):
                l+=1
            else:
                r-=1
        
        return(result)
            
            


