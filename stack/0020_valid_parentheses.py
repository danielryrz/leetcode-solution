class Solution:
    def isValid(self, s: str) -> bool:
        """
        LeetCode 20 - Valid Parentheses

        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
        determine if the input string is valid.

        A string is valid if:
        1. Open brackets must be closed by the same type of brackets.
        2. Open brackets must be closed in the correct order.

        Time Complexity: O(n) we iterate through each char once
        Space Complexity: O(n) only open parentheses are appended to stack. Valid, worst case is that "((((((" half of open parentheses are added to stack, so O(n/2) => O(n)
        """

        stack = []
        matching = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            # If it's a closing bracket
            if char in matching:
                # Stack must not be empty and top must match
                if not stack or stack[-1] != matching[char]:
                    return False
                stack.pop()
            else:
                # Opening bracket
                stack.append(char)

        # Stack should be empty if valid
        return len(stack) == 0
