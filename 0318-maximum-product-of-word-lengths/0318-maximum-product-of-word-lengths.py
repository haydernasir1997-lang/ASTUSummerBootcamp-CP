
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maximum = 0
        
        for i in range(len(words)):
            right = len(words)-1
            for right in range(i + 1, len(words)):
                if not set(words[i]) & set(words[right]):
                    maximum = max(maximum, len(words[i]) * len(words[right]))
                
               
        return maximum


