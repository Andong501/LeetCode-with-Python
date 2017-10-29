#!/usr/bin/env python
# -*- coding: utf-8 -*-

# LeetCode with Python

# You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
# 
# The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.
#
# Example:
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
# Output: [-1,3,-1]

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        dic = {}
        for idx in range(len(nums)):
            dic[str(nums[idx])] = idx
        for num in findNums:
            idx = dic[str(num)]
            get = 0
            for i in nums[idx+1:]:
                if i > num:
                    res.append(i)
                    get = 1
                    break
            if get == 0:
                res.append(-1)
        return res
    
    def nextGreaterElement2(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        dic = {}
        for num in nums:
            while stack and stack[-1]<num:
                dic[stack.pop()] = num
            stack.append(num)
        return [dic.get(num, -1) for num in findNums]

if __name__ = '__main__':
	print Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2])