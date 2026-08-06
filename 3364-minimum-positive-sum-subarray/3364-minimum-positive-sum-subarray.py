class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ms = []

        for i in range(l, r+1):

            ws = sum(nums[:i])

            if ws > 0:
                ms.append(ws)

            for j in range(i, len(nums)):
                ws = ws + nums[j] - nums[j-i]

                if ws > 0:
                    ms.append(ws)

        if not ms:
            return -1

        return min(ms)
       