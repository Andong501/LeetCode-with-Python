#!/usr/bin/env python
# -*- coding: utf-8 -*-

# LeetCode with Python

# TinyURL is a URL shortening service where you enter a URL such as
# 
# Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:
#
# The root is the maximum number in the array.
#
# The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
#
# The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
#
# Construct the maximum tree by the given array and output the root node of this tree.
#
# Example:
# Input: [3,2,1,6,0,5]
# Output: return the tree root node representing the following tree:
#
#      6
#    /   \
#   3     5
#    \    / 
#     2  0   
#       \
#        1

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import operator

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) > 1:
            key,value = max(enumerate(nums), key=operator.itemgetter(1))
            root = TreeNode(value)
            nums_left = nums[:key]
            nums_right = nums[key+1:]
            root.left = self.constructMaximumBinaryTree(nums_left)
            root.right = self.constructMaximumBinaryTree(nums_right)
            return root
        elif len(nums) == 1:
            leaf = TreeNode(nums[0])
            leaf.left = None
            leaf.right = None
            return leaf
        else:
            return None

if __name__ = '__main__':
	print Solution().constructMaxmumBinaryTree([3, 2, 1, 6, 0, 5])
