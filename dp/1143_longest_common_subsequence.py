"""
LeetCode 1143. Longest Common Subsequence

🧩 Problem:
Given two strings text1 and text2, return the length of their longest common subsequence.
A subsequence is a sequence derived from another string by deleting some or no elements 
without changing the order of the remaining characters.

Example:
Input:  text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

---

💡 Approach:
Use dynamic programming (DP) to build a 2D table `dp[i][j]`, where:
    dp[i][j] = length of the longest common subsequence between 
                text1[:i] and text2[:j].

If the current characters match:
    dp[i][j] = dp[i-1][j-1] + 1
Otherwise:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

---

⏱️ Time Complexity:  O(m * n)
💾 Space Complexity: O(m * n)
where m = len(text1), n = len(text2)

---

🚀 Follow-up Optimization:
Since each row in the DP table only depends on the previous row, 
we can reduce the space complexity to O(min(m, n)) by storing only two rows at a time 
(or even one if updated carefully in reverse order).
"""

# -------------------------------------------------------------
#  Standard Dynamic Programming Solution (O(m * n) space)
# -------------------------------------------------------------
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m = len(text1)
        n = len(text2)

        # Initialize a DP table of size (m+1) x (n+1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Build the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    # Characters match → extend previous subsequence (diagonal)
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # Characters don't match → take the best of top or left cell
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Result is the bottom-right cell
        return dp[m][n]


# -------------------------------------------------------------
#  Optimized Dynamic Programming Solution (O(min(m, n)) space)
# -------------------------------------------------------------
"""
Optimized version:
Time Complexity:  O(m * n)
Space Complexity: O(min(m, n))

We only keep two 1D arrays (previous and current rows)
since each dp[i][j] depends only on the previous row and the current row.
"""
def longestCommonSubsequence(self, text1, text2):
    """
    :type text1: str
    :type text2: str
    :rtype: int
    """
    # Ensure text2 is the shorter string to save memory
    if len(text2) > len(text1):
        text1, text2 = text2, text1

    m, n = len(text1), len(text2)

    prev = [0] * (n + 1)
    curr = [0] * (n + 1)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                curr[j] = 1 + prev[j - 1]
            else:
                curr[j] = max(prev[j], curr[j - 1])
        # Move to the next row
        prev, curr = curr, [0] * (n + 1)

    return prev[n]
