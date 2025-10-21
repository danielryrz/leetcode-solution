# Array Problems

### [Jump Game I (#55)](0055_jump_game.py)
Greedy solution with explanation.  
- Time: O(n)  
- Space: O(1)

---

### [Jump Game II (#45)](0045_jump_game_ii.py)
- **Version 1: Greedy (Efficient)**  
  Tracks farthest reachable index (`farthest`) and current jump boundary (`current_end`).  
  Increments jumps when crossing the boundary. It works but it does not track the actual jump indices, thanks to which takes less space O(1), 
  rather then version 2 which tracks the actual jump indices and takes space O(n).
  - Time: O(n)  
  - Space: O(1)  

- **Version 2: Greedy + Path Reconstruction**  
  In addition to counting jumps, it records the actual jump indices.  
  Example: `[2,3,1,1,4] → (2, [0,1,4])`  
  - Time: O(n)  
  - Space: O(n)
