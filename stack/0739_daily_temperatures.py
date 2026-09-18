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

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) #so that 0s are covered by default
        stack = [] # stack to help

        for i in range(len(temperatures)):
            #while stack and temp now is greater than the temp on the index (day) saved at the top of stack - continue until stack is Empty or it is not greater
            while stack and temperatures[i] > temperatures[stack[-1]]:
                #if True then calculate the days difference and save to result, under the corresponding index 
                res[stack[-1]] = i - stack[-1]
                #remove the index stack[-1] as its result is already saved in res
                del stack[-1]

            #if not then append the index i to the stack
            stack.append(i)
        
        return res
