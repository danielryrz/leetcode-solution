class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return False


        countT, window = {}, {}

        for c in t:
            countT[c] = countT.get(c, 0) + 1
        

        res, resLen = [-1,-1], float("inf")
        L = 0
        have, need = 0, len(countT)

        for R in range(len(s)):
            c = s[R]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if (R-L+1) < resLen:
                    resLen = R-L+1
                    res = [L, R]

                window[s[L]] -= 1
                if s[L] in countT and window[s[L]] < countT[s[L]]:
                    have -= 1
                
                L += 1
        L, R = res

        return s[L:R+1] if resLen != float("inf") else ""




