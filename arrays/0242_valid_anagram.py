from typing import Dict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Problem:
        Given two strings s and t, return True if t is an anagram of s, and False otherwise.

        An anagram is a word or phrase formed by rearranging the letters of another word,
        using all the original letters exactly once.

        Approach:
        1. If the lengths of s and t differ, they cannot be anagrams.
        2. Use two hash maps (dictionaries) to count character frequencies in s and t.
        3. Compare the frequency of each character in s with its frequency in t.

        Time Complexity:
        O(n), where n is the length of the strings.
        - One pass to build the frequency maps
        - One pass to compare character counts

        Space Complexity:
        O(1) (or O(k)), where k is the number of distinct characters.
        - For lowercase English letters, k is bounded by 26.
        """

        # Early exit if lengths differ
        if len(s) != len(t):
            return False

        countS: Dict[str, int] = {}
        countT: Dict[str, int] = {}

        # Count character frequencies
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # Compare frequencies
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True
