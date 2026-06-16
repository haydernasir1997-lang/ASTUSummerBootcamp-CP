class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        counts = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and mat[i].count(1)==1:
                    col_count = 0
                    for k in range(len(mat)):
                        col_count += mat[k][j]

                    if col_count == 1:
                        counts += 1

        return counts