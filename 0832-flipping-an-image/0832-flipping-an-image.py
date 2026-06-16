class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        flip = []
        for i in range(len(image)):
            flip.append(image[i][::-1])
            for k in range(len(flip[i])):
                if flip[i][k] == 1:
                    flip[i][k] = 0
                elif flip[i][k] == 0:
                    flip[i][k] = 1

        return flip