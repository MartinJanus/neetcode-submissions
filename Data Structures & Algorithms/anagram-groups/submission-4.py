class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # result = {}
        result = defaultdict(list)
        # creating dictionary defaultdict, its keys will be character-frequency patterns, and its values will be list of waords. 
        # the list means that accessign a missing key automatically creates an empty list


        for word in strs: #visit each string
            count = [0] * 26 #creates a list containing 26 zeros, one for each letter in alphabet lower case

            for char in word: #visit each character in the word
                index = ord(char) - ord("a") # ord() returns character numeric Unicode value, we subtract a, so we are at correct index. 
                count[index] += 1 # increase frequency for each character
            
            key = tuple(count) # creates frequency list into a tuple, list cant be keys in python. immutable 
        
            result[key].append(word) # add groups associated with key, and original word
        
        return list(result.values()) # returning list, coverts dictionary values into a normal list


        # o(m*n) 


        # regular dictionary:
        # result = {}

        # if key not in result:
        #     result[key] = []

        # result[key].append(word)