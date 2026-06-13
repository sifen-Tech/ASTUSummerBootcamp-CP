class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count=0
        for n in nums:
            count+=str(n).count(str(digit))
        return count
            

            
        