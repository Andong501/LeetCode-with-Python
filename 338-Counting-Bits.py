#!/usr/bin/env python
# -*- coding: utf-8 -*-

# LeetCode with Python

# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.
#
# Example:
# For num = 5 you should return [0,1,1,2,1,2].

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        list = [0]
        for i in range(1, num+1):
            list.append(list[i >> 1] + (i & 1)) #list recursion
        return list

if __name__ = '__main__':
	print Solution().countBits(5)
