class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        temp=0
        nums.sort()
        for i in range (len(nums)//2):
            p_sum= nums[i] +nums[len(nums)-1-i]
            temp= max(p_sum,temp)
        return temp
       