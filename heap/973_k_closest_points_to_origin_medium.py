"""
973. K Closest Points to Origin (Medium)
----------------------------------------

You are given an array `points` where points[i] = [x_i, y_i] represents a point 
on the 2D plane. Return the *k* closest points to the origin (0, 0).

The Euclidean distance can be compared using:
    distance^2 = x^2 + y^2
Taking sqrt() is unnecessary because sqrt() is monotonic.

------------------------------------------------------------
Approach 1 — Sorting (brute force)
------------------------------------------------------------
1. Compute squared distance for each point.
2. Store pairs (distance, point).
3. Sort by distance.
4. Return the first k points.

Time Complexity:  O(n log n)
Space Complexity: O(n)

This is easy to understand but slower than the heap solution.
"""

from typing import List

class SolutionSorting:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        dist = []

        # Store pairs (distance, point)
        for x, y in points:
            d = x * x + y * y
            dist.append((d, [x, y]))

        # Sort by distance
        dist.sort(key=lambda x: x[0])

        # Return the k closest points
        return [p for _, p in dist[:k]]



"""
------------------------------------------------------------
Approach 2 — Heap (Optimal)
------------------------------------------------------------
Use a max-heap of size k:
- Store negative distances so Python's min-heap acts like a max-heap.
- Push each point.
- If heap exceeds size k → pop the farthest point.
- At the end, heap contains k closest points.

Time Complexity:  O(n log k)
Space Complexity: O(k)

This approach is optimal for large inputs.
"""

import heapq

class SolutionHeap:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        max_heap = []  # stores (-distance, point)

        for x, y in points:
            d = x * x + y * y

            # Push negative distance to simulate a max-heap
            heapq.heappush(max_heap, (-d, [x, y]))

            # If we have more than k points, remove the farthest
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        # Extract just the points
        return [point for _, point in max_heap]
