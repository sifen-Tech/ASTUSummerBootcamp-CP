class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        transpose=[[0] * len(matrix) for i in range(len(matrix[0]))]
        for r in range (len(matrix)):
            for c in range (len(matrix[0])):
                transpose[c][r]=matrix[r][c]
        for n in transpose:
            n.reverse()
        for r in range(len(matrix)):
            for c in range(len(matrix)):
                matrix[r][c] = transpose[r][c]
        return matrix
        
        