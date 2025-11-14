"""
LeetCode 13. Roman to Integer

Problem Statement:
Roman numerals are represented by seven symbols: I, V, X, L, C, D, and M.
Given a Roman numeral, convert it to an integer.

The rules:
- Normally values are added, e.g., III = 3.
- But when a smaller value appears before a larger one, it is subtracted:
    - IV = 4 (5 - 1)
    - IX = 9 (10 - 1)
    - XL = 40 (50 - 10)
    - XC = 90 (100 - 10)
    - CD = 400 (500 - 100)
    - CM = 900 (1000 - 100)

Return the integer representation.

Approach:
- Use a dictionary to map Roman characters to values.
- Traverse the string:
    - If current value < next value → subtract.
    - Otherwise → add.
- This handles all subtractive rules naturally.

Time Complexity:  O(n)       where n is length of the string.
Space Complexity: O(1)       since dictionary is constant size.
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        n = len(s)

        for i in range(n):
            # If next symbol exists and current value is smaller → subtract
            if i + 1 < n and roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]

        return total
