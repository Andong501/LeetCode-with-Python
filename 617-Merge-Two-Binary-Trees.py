#!/usr/bin/env python
# -*- coding: utf-8 -*-

# LeetCode with Python

# Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.
#
# You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.
#
# Example:
# Input: 
#	Tree 1                     Tree 2                  
#          1                         2                             
#         / \                       / \                            
#        3   2                     1   3                        
#       /                           \   \                      
#      5                             4   7                  
# Output: 
# Merged tree:
#	     3
#	    / \
#	   4   5
#	  / \   \ 
#	 5   4   7
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            tm = TreeNode(t1.val+t2.val)
            tm.left = self.mergeTrees(t1.left, t2.left)
            tm.right = self.mergeTrees(t1.right, t2.right)
        elif t1 and (not t2):
            tm = TreeNode(t1.val)
            tm.left = self.mergeTrees(t1.left, None)
            tm.right = self.mergeTrees(t1.right, None)
        elif (not t1) and t2:
            tm = TreeNode(t2.val)
            tm.left = self.mergeTrees(t2.left, None)
            tm.right = self.mergeTrees(t2.right, None)
        else:
            tm = None
        return tm
    
    def mergeTrees2(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if (not t2):
            return t1
        elif (not t1):
            return t2
        else:
            tm = TreeNode(t1.val+t2.val)
            tm.left = self.mergeTrees(t1.left, t2.left)
            tm.right = self.mergeTrees(t1.right, t2.right)
            return tm

if __name__ = '__main__':
	print Solution().mergeTrees([1, 3, 2, 5], [2, 1, 3, null, 4, null, 7])
