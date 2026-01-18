from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        LeetCode 56 — Merge Intervals

        Problem Description:
        You are given an array of intervals where intervals[i] = [start_i, end_i].
        Merge all overlapping intervals and return an array of the non-overlapping
        intervals that cover all the intervals in the input.

        Approach:
        1. Sort the intervals by their start time.
        2. Initialize the output list with the first interval.
        3. Iterate through the remaining intervals:
           - If the current interval overlaps with the last interval in output,
             merge them by extending the end.
           - Otherwise, append the current interval to output.

        Time Complexity:
        - Sorting the intervals takes O(n log n)
        - Merging intervals in a single pass takes O(n)
        - Overall Time Complexity: O(n log n)

        Space Complexity:
        - Output list can store up to n intervals in the worst case
        - Overall Space Complexity: O(n)
        """

        # Sort intervals by start time
        intervals.sort(key=lambda i: i[0])

        # Edge case: initialize output with the first interval
        output = [intervals[0]]

        # Iterate through the remaining intervals
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]  # end of the last interval in output

            # If the current interval overlaps with the last interval
            if start <= lastEnd:
                # Merge by extending the end to the maximum of both ends
                output[-1][1] = max(lastEnd, end)
            else:
                # No overlap: append the current interval
                output.append([start, end])

        return output
