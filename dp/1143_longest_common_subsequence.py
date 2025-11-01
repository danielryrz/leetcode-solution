"""
LeetCode 1143. Longest Common Subsequence

Problem:
Given two strings text1 and text2, return the length of their longest common subsequence.
A subsequence is a sequence derived from another string by deleting some or no elements 
without changing the order of the remaining characters.

Example:
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Approach:
Use dynamic programming (DP) to build a table dp[i][j] where dp[i][j] represents 
the length of the longest common subsequence between text1[:i] and text2[:j].
If the current characters match, extend the subsequence by 1 (dp[i-1][j-1] + 1).
Otherwise, take the maximum of skipping one character from either string.

Time Complexity: O(m * n)
Space Complexity: O(m * n)
where m = len(text1), n = len(text2)

Follow-up Optimization:
Since each row in the DP table only depends on the previous row, 
we can reduce the space complexity to O(min(m, n)) by storing only two rows at a time 
(or even one if updated carefully in reverse order).
"""

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # no. of rows
        m = len(text1)

        # no. of cols
        n = len(text2)

        # add +1 in rows and cols to make handling base case easier
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # if letters match, take the best matching previous subsequence (diagonal left)
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                # else take max and either ignore char from text1 ([i-1]) or ignore char from text2 ([j-1])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]  # take the last value
