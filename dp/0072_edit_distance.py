class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # rows
        m = len(word1)

        # cols
        n = len(word2)

        # Initiatie DP table (m+1) x (n+1) (+1 as we want to store empty string at the beginning of each word)
        dp = [[0]*(n+1) for _ in range(m+1)]

        # col 0 set to i. 
        # I.e. how many ops do we need to convert word1[:i] into an empty string ""
        for i in range(m+1):
            dp[i][0] = i

        # row 0 set to j
        # I.e. how many ops do we need to convert emptry string "" into word2[:j]
        for j in range(n+1):
            dp[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] #just rewrite the no. of ops until now
                
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) # 1 (ops at this point) + min of the previous available ops
        
        return dp[m][n]

        
