class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #need the largest width, multiplied by the smallest of the two heights to form the total area.


        # need to keep track of index and value 

        l = 0 
        r = len(heights)-1 

        # width = l - r
        maximum = []
        # height = min(heights[l], heights[r])
        # maxArea = width*height
        # abs() get absolute value. 
        # print(maxArea)
        # for i, h in enumerate(heights):

        while l < r: 
            height = min(heights[l], heights[r])
            width = l - r
            maxArea = abs(width*height)
            maximum.append(maxArea)
            if (heights[l] < heights[r]):
                l+=1
            else:
                r-=1
        
        return(max(maximum))
            
            


