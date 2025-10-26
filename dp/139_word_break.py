def wordBreak(s, wordDict):
    word_set = set(wordDict)

    # dp[i] means "can we segment s[:i] ?"  (i from 0 to len(s))
    dp = [False] * (len(s) + 1)
  
    # empty prefix is segmentable
    dp[0] = True  

    # check prefix lengths 1..len(s)+1
    for i in range(1, len(s) + 1):            
        for w in word_set:

            # word fits into prefix of length i               
            if len(w) <= i: 
                                
                # check the prefix BEFORE this word is good
                if dp[i - len(w)] and s[i - len(w):i] == w:
                    dp[i] = True         # s[:i] is segmentable
                    break                # no need to try other words for this i -> move to the next word
    return dp[-1] #check the last dp value: either True or False
