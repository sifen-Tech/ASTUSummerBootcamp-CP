from collections import*
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        for i in strs:
            key="".join(sorted(i))
            my_dict[key].append(i)
        arr=[]
        for val in my_dict.values():
            arr.append(val)
        return arr