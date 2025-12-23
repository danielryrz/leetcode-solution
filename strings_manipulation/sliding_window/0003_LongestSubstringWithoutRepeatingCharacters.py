# 3. Longest Substring Without Repeating Characters
# Difficulty: Medium
#
# Problem:
# Given a string s, return the length of the longest substring without 
# repeating characters.
#
# Example:
# Input:  s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with length 3
#
# Approach:
# Use the sliding window technique:
# - Maintain a window that always contains unique characters using a HashSet.
# - Expand the right pointer to add characters.
# - If a duplicate appears, move the left pointer until the duplicate is removed.
#
# Time Complexity: O(n), because each character is visited at most twice.
# Space Complexity: O(min(n, k)), where k is the character set size.
# 
# Category: Sliding Window / HashSet / Strings

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            # If character repeats, shrink window until it's removed
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Add current character and update max length
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len


