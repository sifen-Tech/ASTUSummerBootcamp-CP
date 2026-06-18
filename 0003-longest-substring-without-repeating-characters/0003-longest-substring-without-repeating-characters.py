from collections import *
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left =0 
        max_window =0
        
        window = defaultdict(int)
        for i in range (len(s)):
            window [s[i] ]+=1
            while window [s[i]] >1 :
                window[s[left]] -=1
                if window [s[left]] == 0 :
                    del window[s[left]]
                left+=1
            max_window= max( max_window , i - left+1   ) 
        return max_window       