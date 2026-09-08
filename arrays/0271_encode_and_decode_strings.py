class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s   # we first write the len then "#" then string s. eg for "cat": "3#cat"
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0 #create res list and set pointer i to 0 

        while i < len(s): #while pointer i inbound
            j = i #set new pointer j to find the "#" so we can get the length of the string
            while s[j] != "#":
                j += 1 #increase j until we find "#"
            length = int(s[i:j]) # the length is characters between i and j (it can be larger than 9, eg. 872, so more than one figure)
            res.append(s[j+1:j+1+length]) #append the list by writing in the s
            i = j + 1 + length # increase i 
        
        return res
