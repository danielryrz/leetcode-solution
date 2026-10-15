class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        L = 0
        res = 0

        for R in range(len(s)):
            if s[R] in mp:
                L = max(mp[s[R]] + 1, L) # move L to the index of saved s[R] + 1 or keep at L - whichever is greater
                # mp.remove(s[R])
            
            mp[s[R]] = R
            res = max(res, R - L + 1)
        

        return res
