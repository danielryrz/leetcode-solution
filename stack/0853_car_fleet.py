class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        
        cars = sorted(zip(position, speed), reverse=True) #sort together poision and speed list in descending order - so that we can start from the car that is closest to the target

        for p,s in cars:
            t = (target - p) / s
            stack.append(t)
          
            if len(stack) >= 2 and stack[-1]<= stack[-2]:
                stack.pop() #pop - add the current car to the fleet
        
        return len(stack)
  
