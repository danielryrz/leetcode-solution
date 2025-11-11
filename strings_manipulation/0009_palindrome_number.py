"""
LeetCode Problem 9: Palindrome Number
--------------------------------------------
Given an integer x, return true if x is a palindrome, and false otherwise.

Examples:
----------
Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

-----------
Version 1: Converting int to str and comparing char one by one

Time Complexity:  O(n), where n = len(x)
Space Complexity: O(n), where n = len(x)

-----------
Version 2: Appending the reverse starting from 0 with the last digits of x

Time Complexity:  O(n), where n = len(x)
Space Complexity: O(1), fixed nr of vars, it doesn't grow

"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)[::1] == str(x)[::-1]


#--------------
# Version 2:
#--------------
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        #-ve int is not a palindrome
        if x < 0:
            return False

        #if the int ends with 0, for it to be a palindrome, it needs to start with 0
        #only 0 itself satisfies this
        if x % 10 == 0 and x != 0:
            return False 

        #do the revert algorithm

        original = x
        reverse = 0

        while x > 0:
            #get the last digit
            last_digit = x % 10 

            #Append the last digit to reverse
            reverse = (reverse * 10) + last_digit

            #remove the last digit from n
            x = x // 10
        
        return (reverse == original)

