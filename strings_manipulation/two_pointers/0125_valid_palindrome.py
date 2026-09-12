# sol3 -preferred Time O(n), Space O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1

        # L<R as L == R is valid by default if the len(s) % 2 == 0 (is odd) 
        while L < R:
            while L < R and not s[L].isalnum():
                L += 1
            while L < R and not s[R].isalnum():
                R -= 1
            if s[L].lower() != s[R].lower():
                return False
            L += 1
            R -= 1
        return True 


# sol 2 Time O(n) Space O(n). newStr += c.lower() operation is not preferred
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         newStr = ""

#         for c in s:
#             if c.isalnum():
#                 newStr += c.lower()
        
#         return newStr == newStr[::-1]


# sol 1  Time O(n) Space O(n)
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = ''.join(filter(str.isalnum, s)).lower()
#         # s = s.lowercase()
        
#         if s == "":
#             return True
        
#         elif len(s) % 2  == 0: #even len
#             L = (len(s) - 1) // 2
#             R = (len(s) - 1) // 2 + 1
#             while L >= 0 and R <= (len(s) - 1):
#                 if s[L] == s[R]:
#                     L -= 1
#                     R += 1
#                 else:
#                     return False
#             return True

#         elif len(s) % 2 != 0: #odd len
#             L = len(s) // 2
#             R = len(s) // 2
#             while L >= 0 and R <= (len(s) - 1):
#                 if s[L] == s[R]:
#                     L -= 1
#                     R += 1
#                 else:
#                     return False
#             return True

        
