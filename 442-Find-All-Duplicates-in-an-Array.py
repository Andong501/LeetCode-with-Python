#!/usr/bin/env python
# -*- coding: utf-8 -*-

# LeetCode with Python

# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
# 
# Find all the elements that appear twice in this array.
# 
# Could you do it without extra space and in O(n) runtime?
#
# Example:
# Input:
# [4,3,2,7,8,2,3,1]
# 
# Output:
# [2,3]

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        return [nums[i] for i in range(len(nums)-1) if nums[i]==nums[i+1]]
    
    def findDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for num in nums:
            if nums[abs(num)-1]<0:
                res.append(abs(num))
            else:
                nums[abs(num)-1] *= -1
        return res

if __name__ = '__main__':
	print Solution().findDuplicates([4,3,2,7,8,2,3,1])