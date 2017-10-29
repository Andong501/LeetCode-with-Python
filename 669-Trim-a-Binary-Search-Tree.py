#!/usr/bin/env python
# -*- coding: utf-8 -*-

# LeetCode with Python

# Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L). You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.
#
# Example:
# Input: 
#    3
#   / \
#  0   4
#   \
#    2
#   /
#  1
#
#  L = 1
#  R = 3
#
#Output: 
#      3
#     / 
#   2   
#  /
# 1

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        root = self.trimBST_L(root, L)
        root = self.trimBST_R(root, R)
        return root
        
    def trimBST_L(self, root, L): #only for left
        if L < root.val:
            if root.left:
                root.left = self.trimBST_L(root.left, L)
        elif L == root.val:
            if root.left:
                root.left = None
        else: # if L > root.val
            if root.right:
                root = self.trimBST_L(root.right, L)
            else:
                root = None
        return root
    
    def trimBST_R(self, root, R): #only for right
        if R > root.val:
            if root.right:
                root.right = self.trimBST_R(root.right, R)
        elif R == root.val:
            if root.right:
                root.right = None
        else: # if R < root.val
            if root.left:
                root = self.trimBST_R(root.left, R)
            else:
                root = None
        return root

if __name__ = '__main__':
	print Solution().trimBST([1, 0, 2], 1, 2)
