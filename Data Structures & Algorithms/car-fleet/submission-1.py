class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack=[]
        pairs = list(zip(position, speed))
        pairs.sort(reverse=True)
        for p,s in pairs: 
                arrivalTime = (target - p) / s
                if not stack:
                    stack.append(arrivalTime)
                if stack and stack[-1] < arrivalTime:
                    print("here")
                    stack.append(arrivalTime)
  

        print(stack)
        return len(stack)
        # Input: target = 10, position = [1,4], speed = [3,2]


        # 10-4=6/2 = 3 
        # 10-1=9/3 = 3 

        # Target 10 
        # (2 fleets)
        # car1 = 1,4,7,10
        # car2 = 4,6,8,10

        # 1 fleet


        # Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]

        # Output: 3

        # car1=4,6,8,10
        # car2=1,3,5,7,9,11 (dont catch up)
        # car3=0,1,2,3,4,5,6,7,8,9,10 (dont catch up)
        # car4=7,8,9,10

        # 3 fleets


        # arrivalTime = Target - Position / Speed 

        #we use a stack to get the MinimumTime it takes to get to the target per car. 
        #sort by position of car. 
        #basically we compare the top of the stack to the next car 
        # (10 - 4 / 2) = 3
        # (9/2)=5 






        
        
