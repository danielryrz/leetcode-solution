"""
LeetCode 981. Time Based Key-Value Store
----------------------------------------

Design a data structure that supports:

1. set(key, value, timestamp)
   - Stores the key with the given value and timestamp.
   - Timestamps for each key are strictly increasing.

2. get(key, timestamp)
   - Returns the value with the largest timestamp <= given timestamp.
   - If no such timestamp exists, return "".

Approach:
- Use a dictionary mapping each key to a list of (timestamp, value) pairs.
- Append on set() because timestamps are always increasing.
- Use binary search on get() to find the rightmost timestamp <= target.

Time Complexity:
- set(): O(1) average (append to list)
- get(): O(log n) for binary search on timestamps

Space Complexity:
- O(n) for storing all (timestamp, value) pairs
"""


class TimeMap:

    def __init__(self):
        # Maps key -> list of (timestamp, value)
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        # Append because timestamps are strictly increasing
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        arr = self.store[key]
        left, right = 0, len(arr) - 1
        result = ""

        # Binary search for largest timestamp <= given timestamp
        while left <= right:
            mid = (left + right) // 2
            t, v = arr[mid]

            if t == timestamp:
                return v
            elif t < timestamp:
                result = v      # candidate
                left = mid + 1
            else:
                right = mid - 1

        return result
