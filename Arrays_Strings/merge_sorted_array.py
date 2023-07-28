# Since we know nums1 has exactly enough space for nums1 and num2, we can start from the end of the array
# and work backwards.

# We can simply insert the elements of nums2 into nums1 and then sort nums1 with the built-in sort() method.

# Remember to decrement j by 1 each time we insert an element from nums2 into nums1.

# Time Complexity: O(n)
# Space Complexity: O(1)


# My solution
class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        j = -1
        for i in nums2:
            nums1[j] = i
            j -= 1
        nums1.sort()


# Alternative solution (NeetCode)
class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        # Last index nums1
        last = m + n - 1

        # Merge in reverse order
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1
        
        # Add missing elements from nums2
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1
        

# Copy and paste this into LeetCode to test
