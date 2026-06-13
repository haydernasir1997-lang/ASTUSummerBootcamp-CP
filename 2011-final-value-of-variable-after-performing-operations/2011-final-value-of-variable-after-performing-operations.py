class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        counts = 0
        for i in operations:
            if i == "--X" or i=="X--" :
                counts -= 1
            elif i == "++X" or i=="X++":
                counts += 1
        return counts
    
