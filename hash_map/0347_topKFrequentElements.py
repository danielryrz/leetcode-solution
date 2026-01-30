#################
# Method 0
# Built with dictionary, without Counter
################

def topKFrequent(nums, k):

    #Example nums = [1,1,1,2,2,3] ; k = 2
    #set a dictionary to store the count of each of the int
    count = {} 

    # built a freq list consisting of empty lists of len(nums) + 1 to later store the int for the corresponding freq
    freq = [ [] for i in range(len(nums) + 1) ]  

    for n in nums:
        count[n] = 1 + count.get( n, 0)

    #Now the count = {1:3, 2:2, 3:1}

    for n, c in count.items:() # key:value pair
        freq[c].append(n)

    #Now the freq = [ [],[1],[2],[1],[],[],[] ]

    res = [] #create list for results

    for i in range(len(freq)-1, 0, -1): #start from the end and move by 1 to the start
        for n in freq[i]: #acts only if the freq[i] is not an empty list
            res.append(n)
            if len(res) == k:
                return res
            
        



from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        LeetCode 347. Top K Frequent Elements
        
        Approach:
        ---------
        We use a Bucket Sort–based method to achieve O(n) time complexity.
        1. Count the frequency of each number.
        2. Create buckets where index = frequency.
        3. Traverse buckets from highest frequency down until we collect k elements.

        This avoids sorting the frequency list (which would be O(n log n))
        and satisfies the follow-up requirement: better than O(n log n).

        Parameters:
        -----------
        nums : List[int]
            The list of integers.
        k : int
            The number of most frequent elements to return.

        Returns:
        --------
        List[int]
            The k elements with the highest frequency.
        """

        # Step 1: Count each number's frequency
        freq = Counter(nums)  # e.g., {num: count}

        # Step 2: Create buckets where index = frequency
        # Max frequency cannot exceed len(nums), so allocate len(nums) + 1 buckets.
        buckets = [[] for _ in range(len(nums) + 1)]
        
        # Place numbers into the corresponding bucket
        for num, count in freq.items():
            buckets[count].append(num)

        # Step 3: Build the result by scanning buckets from highest frequency
        result = []
        for count in range(len(buckets) - 1, 0, -1):
            for num in buckets[count]:
                result.append(num)
                if len(result) == k:
                    return result

        # Should never reach here since k is always valid
        return result

#-----------------------------------
# Another way to solve it - Method 2
# Note: not preferred, slower
#-----------------------------------

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Time complexity: O(n + k*n)
        Space complexity: O(n)
        """
        freq = {}
        res = []

        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        
        while k > 0:
            res.append(max(freq, key=freq.get))
            freq.pop(res[-1])
            k -= 1
        
        return res

