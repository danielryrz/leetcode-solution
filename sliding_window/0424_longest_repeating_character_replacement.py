class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        L, res, maxf = 0, 0, 0

        for R in range(len(s)):
            count[s[R]] = count.get(s[R], 0) + 1
            maxf = max(maxf, count[s[R]]) #update maxf

            while R-L+1-maxf > k:
                count[s[L]] -= 1
                L += 1

            res = max(res, R-L+1)

        return res 

