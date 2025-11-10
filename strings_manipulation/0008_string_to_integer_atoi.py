"""
LeetCode Problem 8: String to Integer (atoi)
--------------------------------------------
Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

Rules:
1. Read in and ignore any leading whitespace.
2. Check if the next character is '+' or '-'. Determine the sign.
3. Read in the next characters until the next non-digit character or end of input.
4. Convert those digits into an integer.
5. Clamp the result to the 32-bit signed integer range:
       [-2^31, 2^31 - 1] = [-2147483648, 2147483647]
6. Return the final integer.

Example:
----------
Input: s = "   -42"
Output: -42

Explanation:
The function reads the first non-whitespace character '-', then reads the digits '42',
producing the integer -42.

Time Complexity:  O(n), where n = len(s)
Space Complexity: O(1)
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Trim leading whitespaces
        s = s.lstrip()
        if not s:
            return 0

        # Step 2: Determine sign
        sign = 1
        i = 0
        if s[0] in ['-', '+']:
            sign = -1 if s[0] == '-' else 1
            i += 1

        # Step 3: Convert digits to integer
        num = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        # Step 4: Apply sign
        num *= sign

        # Step 5: Clamp to 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num
