from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        Problem:
        --------
        Given an array of package weights and an integer 'days', return the minimum
        ship capacity required to ship all packages within 'days' days.

        Key Insight:
        ------------
        - The minimum possible capacity must be at least max(weights),
          otherwise the heaviest package would not fit.
        - The maximum possible capacity is sum(weights), which ships everything in one day.
        - The feasibility of a capacity is monotonic:
          If capacity C works, any capacity > C will also work.
        - Therefore, binary search can be applied on the capacity range.

        Time Complexity:
        ----------------
        O(n * log(sum(weights)))
        - Binary search over the capacity range: log(sum(weights))
        - Each feasibility check scans all weights: O(n)

        Space Complexity:
        -----------------
        O(1)
        - Only constant extra variables are used.
        """

        L = max(weights)              # Minimum possible capacity
        R = sum(weights)              # Maximum possible capacity
        res = R

        while L <= R:
            c = (L + R) // 2          # Candidate capacity

            cargo = 0
            d = 1                    # Start with day 1

            for weight in weights:
                cargo += weight

                if cargo <= c:
                    pass
                else:
                    d += 1           # Need an extra day
                    cargo = weight   # Start new day with current package

            # Capacity c is feasible, as allows to ship weights in d <= days
            # Search for smaller c
            if d <= days:
                R = c - 1
                res = min(c, res)

            # Capacity c requires ship to operate more days than possible (d > days)
            # Infeasible -> search for larger c
            else:
                L = c + 1

        return res
