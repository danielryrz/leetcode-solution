"""
LeetCode 739 - Daily Temperatures

Problem Statement:
Given an array of integers `temperatures` where temperatures[i] represents
the temperature on the i-th day, return an array `answer` such that:

    answer[i] is the number of days you have to wait after the i-th day
    to get a warmer temperature.

If there is no future day for which this is possible, answer[i] should be 0.

Example:
Input:  temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]


Approach (Monotonic Decreasing Stack):
We use a stack to store indices of days whose warmer temperature has not yet
been found.

The stack maintains a decreasing order of temperatures:
- Each index in the stack represents a day waiting for a warmer temperature.
- When a warmer temperature is found, we pop indices from the stack and compute
  the number of days waited.

Why it works:
- Each index is pushed onto the stack once and popped once.
- This guarantees linear time complexity.


Time Complexity:
O(n)
Each index is pushed and popped at most once.

Space Complexity:
O(n)
The stack can store up to n indices in the worst case.
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n #create default answer List
        stack = []  # stack holds indices of unresolved days

        for i in range(n):
            # Resolve all previous days that are colder than today
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                answer[prev_day] = i - prev_day

            # Add current day index to the stack
            stack.append(i)

        return answer
