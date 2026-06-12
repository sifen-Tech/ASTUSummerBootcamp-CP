class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        flipped=[row[::-1] for row in image] 
        for row in flipped:  
           for i in range(len(row)):
                 row[i] = 1 - row[i]       
        return flipped
               


        