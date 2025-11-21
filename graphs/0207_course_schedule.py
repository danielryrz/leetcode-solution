# 🧠 Problem: 207. Course Schedule
# ------------------------------------------------------------
# There are a total of `numCourses` courses you have to take, labeled from 0 to numCourses - 1.
# You are given an array `prerequisites` where prerequisites[i] = [a, b] 
# indicates that you must take course `b` before course `a`.
#
# Return True if it is possible to finish all courses, otherwise return False.
#
# Example:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: True
# Explanation: You can take course 0, then course 1.
#
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: False
# Explanation: You must take both 0 and 1 first — impossible (cycle).
#
# ------------------------------------------------------------
# 🧩 Approach:
# This is a classic **Topological Sort** problem, which can be solved using:
# - **BFS (Kahn’s Algorithm)** or
# - **DFS cycle detection**.
#
# We'll use **BFS (Kahn's Algorithm)**:
# 1. Build an adjacency list for the graph.
# 2. Compute in-degrees (number of prerequisites) for each course.
# 3. Add all courses with in-degree 0 to a queue (no prerequisites).
# 4. Repeatedly remove a course from the queue and reduce the in-degree
#    of its dependent courses by 1.
# 5. If all courses are processed, return True; otherwise, there’s a cycle → False.
#
# ------------------------------------------------------------
# 🕒 Time Complexity: O(V + E)
#   - V = numCourses (vertices)
#   - E = number of prerequisite pairs (edges)
# Each node and edge is processed once.
#
# 💾 Space Complexity: O(V + E)
#   - Adjacency list and in-degree array.
#
# ------------------------------------------------------------

from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Build graph
        adj = {i: [] for i in range(numCourses)}  # adjacency list
        indegree = [0] * numCourses              # track number of prereqs for each course

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1

        # Step 2: Initialize queue with all courses having no prerequisites
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        # Step 3: Process the queue
        taken_courses = 0

        while queue:
            current = queue.popleft()
            taken_courses += 1  # You can now "take" this course

            # Reduce in-degree for all courses dependent on the current course
            for neighbor in adj[current]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: If we managed to take all courses, return True
        return taken_courses == numCourses
