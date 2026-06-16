class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l=[]
        r=[]
        temp=[]
        for num in nums:
            if num < pivot:
                l.append(num)
            elif num > pivot:
                r.append(num)
            else:
                temp.append(num)
        return l+ temp+ r
            


        