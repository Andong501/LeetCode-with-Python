#!/usr/bin/env python
# -*- coding: utf-8 -*-

# LeetCode with Python

# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution(object):
	#time: O(n^2)
	def twoSum(self, nums, target):
		for i in range(0, len(nums)-1):
			for j in range(i+1, len(nums)):
				if nums[i] + nums[j] == target:
					return [i, j]
		return []
	#time: O(n)
	def twoSumBetter(self, nums, target):
		lookup = {}
		for i, num in enumerate(nums):
			if target - num in lookup:
				return [lookup[target-num], i]
			lookup[num] = i
		return []

if __name__ = 'main':
	print Solution().twoSum([2, 7, 11, 15], 9)