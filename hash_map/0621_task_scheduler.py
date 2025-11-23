"""
621. Task Scheduler
-------------------
You are given an array of tasks, each represented by a capital letter.
Each task takes 1 unit of time. Each identical task must be separated
by at least `n` units of cooldown time. During the cooldown you may
either run a different task or stay idle.

Return the minimum number of intervals required to finish all tasks.

Approach:
---------
We use a frequency counting strategy. The idea is that the task(s)
with the highest frequency determine the minimum schedule length.
If `maxFreq` is the highest task count, and `maxCount` is how many
tasks appear exactly `maxFreq` times, then:

Minimum intervals needed:
    (maxFreq - 1) * (n + 1) + maxCount

Finally, the result must be at least the number of tasks, since
having many tasks may fill all idle slots.

Time Complexity:
----------------
O(n), where n = number of tasks, because we count frequencies and
compute the result using a constant set of operations.

Space Complexity:
-----------------
O(1), because we store at most 26 counts for A–Z, which is constant.
"""

class Solution:
    def leastInterval(self, tasks, n):
        from collections import Counter
        
        # Count how many times each task appears
        freq = Counter(tasks)
        
        # Find the max frequency
        maxFreq = max(freq.values())
        
        # Count how many tasks appear maxFreq times
        maxCount = sum(1 for v in freq.values() if v == maxFreq)
        
        # Apply the scheduling formula
        part_count = maxFreq - 1
        part_length = n + 1
        empty_slots = part_count * part_length + maxCount
        
        # Final answer must cover at least all tasks
        return max(len(tasks), empty_slots)
