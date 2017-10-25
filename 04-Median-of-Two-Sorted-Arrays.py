#!/usr/bin/env python
# -*- coding: utf-8 -*-

# LeetCode with Python

# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# Example 1:
#
#nums1 = [1, 3]
#nums2 = [2]
#The median is 2.0
#
# Example 2:
#
#nums1 = [1, 2]
#nums2 = [3, 4]
#The median is (2 + 3)/2 = 2.5

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        if (len1+len2)%2 == 1:
            return self.getKth(nums1, nums2, (len1+len2)/2+1)
        else:
            return (self.getKth(nums1, nums2, (len1+len2)/2) + self.getKth(nums1, nums2, (len1+len2)/2+1))/2.0
    
    # find the Kth num
    def getKth(self, nums1, nums2, k):
        len1 = len(nums1)
        len2 = len(nums2)
        if len2 < len1:return self.getKth(nums2, nums1, k)
        if len1 == 0:return nums2[k-1]
        if k == 1:return min(nums1[0], nums2[0])
        pa = min(k/2, len1)
        pb = k -pa
        if nums1[pa-1]<=nums2[pb-1]:
            return self.getKth(nums1[pa:], nums2, pb)
        else:
            return self.getKth(nums1, nums2[pb:], pa)

if __name__ = '__main__':
	print Solution().findMedianSortedArrays([1, 3], [2, 4])