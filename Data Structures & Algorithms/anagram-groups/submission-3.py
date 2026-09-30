class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # result = {}
        result = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for char in word:
                index = ord(char) - ord("a")
                count[index] += 1
            
            key = tuple(count)

            result[key].append(word)
        
        return list(result.values())