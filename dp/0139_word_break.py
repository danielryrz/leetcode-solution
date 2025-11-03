class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # from list -> make a set for improved performance. Search for words reduced from O(n) to O(1)
        # remove duplicates, if any present 
        words = set(wordDict)

        # Create dp row of length len(s) + 1 as we want to store value for an empty string
        dp = [False] * (len(s) + 1)

        # Set True value to an empty string. We can refer to its True value when checking the next word (I.e. dp[i-len(w)] = dp[0] == True -> Yes if word w meets the criteria
        dp[0] = True
        

        for i in range(1,len(s)+1):
            for w in words:
                # if len(w) <= i (can i is long enough to create a word w) and s[i-len(w):i] == w (is the word formed == w) and is the previous value at [dpi-len(w)]==True
                if len(w) <= i and s[i-len(w):i] == w and dp[i-len(w)] == True:
                    dp[i] = True
                    break # move to the next w 
        
        return dp[-1] # return the last boolean value 
