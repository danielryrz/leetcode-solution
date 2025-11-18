"""
LeetCode 5. Longest Palindromic Substring

----------------------------------------
📘 Problem Statement
Given a string s, return the longest palindromic substring in s.

A substring is a contiguous sequence of characters within a string.
A palindrome reads the same forward and backward.

----------------------------------------
⏱ Time Complexity
O(n^2) — For each character, we expand outward in both directions,
and the expansion takes O(n) in the worst case.

💾 Space Complexity
O(1) — We only store pointers and the current longest substring.

----------------------------------------
📌 Approach: Expand Around Center
A palindrome mirrors around its center. The center can be:
• a single character (odd-length palindrome)
• between two characters (even-length palindrome)

For each index i:
1) Expand around center (i, i) for odd palindromes
2) Expand around center (i, i+1) for even palindromes
Track and return the longest palindrome seen.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:

        # Helper function: expand outward while characters match
        def expand_around_center(L, R, s):
            # Expand as long as we stay within bounds and characters match
            while L >= 0 and R < len(s) and s[L] == s[R]:
                L -= 1
                R += 1
            # L and R went one step too far, so return the valid substring
            return s[L+1:R]

        longest = ""

        # Check palindromes centered at every index
        for i in range(len(s)):
            # Odd-length palindrome (centered at i)
            p1 = expand_around_center(i, i, s)
            
            # Even-length palindrome (centered between i and i+1)
            p2 = expand_around_center(i, i+1, s)

            # Update the longest palindrome found
            if len(p1) > len(longest):
                longest = p1
            if len(p2) > len(longest):
                longest = p2
        
        return longest
