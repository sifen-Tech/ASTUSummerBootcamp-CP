class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans=0
        for n in range (len(nums)):
            temp =[]
            for i in range (n,len(nums)):
                if nums[i] > threshold :
                    break
                if len(temp)==0:
                    if nums[i]%2==0:
                        temp.append(nums[i])
                else:
                    if nums[i]%2 != temp[-1]%2:
                        temp.append(nums[i])
                    else:
                        break
            ans = max(ans,len(temp))
        return ans

                            
                
            
       