class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import operator as op 
        stack = []
        ops = {
            "+": op.add,
            "-": op.sub,
            "*": op.mul,
            "/": lambda a,b : int(a/b) #to ensure it truncates to zero
        }

        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[t](a, b))
        
        return stack.pop()
            
        
