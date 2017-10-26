#!/usr/bin/env python
# -*- coding: utf-8 -*-

# LeetCode with Python

# Given an array of 2n integers, your task is to group these integers into n pairs of integer, 
#
# say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
#
# Note:
# n is a positive integer, which is in the range of [1, 10000].
# All the integers in the array will be in the range of [-10000, 10000].
#
# Example:
# Input: [1,4,3,2]
# Output: 4
# Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
#
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        nums.sort()
        for i in range(len(nums)/2):
            sum += nums[2*i]
        return sum

    def arrayPairSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])

if __name__ = '__main__':
	print Solution().arrayPairSum([1, 4, 3, 2])
