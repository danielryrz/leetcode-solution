def wordBreak(self, s: str, wordDict: List[str]) -> bool:
  wordSet = set(wordDict)
  dp = [False] * (len(s) + 1)
  dp[0] = True
  
  for i in range(1, len(s)+1):
    for w in wordSet:
        if len(w) <= i and s[i-len(w):i] == w and dp[i-len(w)] :
            dp[i] = True
            break
  
  return dp[-1]
