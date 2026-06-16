class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        matrics_trasposed = []

        for i in range(len(matrix[0])):
            transpose = []

            for k in range(len(matrix)):
                transpose.append(matrix[k][i])

            matrics_trasposed.append(transpose)  

        return matrics_trasposed


