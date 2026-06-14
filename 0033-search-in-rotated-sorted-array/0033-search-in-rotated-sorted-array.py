class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range (len(set(nums))):
            if target == nums[i]:
                return i
        return -1
        