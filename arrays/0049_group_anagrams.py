"""
Problem: Group Anagrams (LeetCode 49)

Given an array of strings `strs`, group the anagrams together.
You can return the answer in any order.

An anagram is a word formed by rearranging the letters of another word,
using all the original letters exactly once.

Example:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

Approach:
- Use a hashmap where:
    key   = character frequency count (tuple of size 26 for 'a' to 'z')
    value = list of strings that share the same character count
- For each string:
    - Build a frequency array of length 26
    - Convert it to a tuple (hashable) and use it as the key
    - Append the string to the corresponding group
- Finally, return all grouped values

Time Complexity:
- Let n = number of strings
- Let k = maximum length of a string
- Counting characters for each string takes O(k)
- Total Time: O(n * k)

Space Complexity:
- Hash map stores up to n keys, each with a tuple of size 26
- Output also stores all input strings
- Total Space: O(n * 26) ≈ O(n)
"""

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # mapping charCount -> list of anagrams

        for s in strs:
            count = [0] * 26  # a...z

            for c in s:
                count[ord(c) - ord('a')] += 1  # map char to index 0-25

            res[tuple(count)].append(s)

        return list(res.values())
