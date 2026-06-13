class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=1
        for k in range(1,len(nums)):
            if nums[k]!= nums[k-1]:
                nums[l]=nums[k]
                l+=1
        return l
        