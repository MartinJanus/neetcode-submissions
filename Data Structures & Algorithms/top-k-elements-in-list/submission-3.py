class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequentnums = {}

        for i in nums: 
            frequentnums[i] = frequentnums.get(i,0)+1
        

        orderednums = sorted(frequentnums, key=frequentnums.get, reverse = True)
        print(orderednums)


        result = orderednums[:k] 
        return(result)



            