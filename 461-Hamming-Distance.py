#!/usr/bin/env python
# -*- coding: utf-8 -*-

# LeetCode with Python

# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#
# Given two integers x and y, calculate the Hamming distance.
#
# Note:
# 0 ≤ x, y < 2^31.
#
# Example:
# Input: x = 1, y = 4
# 
# Output: 2
# 
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
#

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xcode = self.getBinaryCode(x, code=[0]*31)
        ycode = self.getBinaryCode(y, code=[0]*31)
        dis = sum(x!=y for x, y in zip(xcode, ycode))
        return dis
    
    def getBinaryCode(self, x, code):
        if x > 0:
            for i in range(31):
                if (x>=2**i) and (x<2**(i+1)):
                    code[i] = 1
                    break
            x = x - 2**i
            code = self.getBinaryCode(x, code)
        return code
    
    def hammingDistance2(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')

if __name__ = '__main__':
	print Solution().hamingDistance(1, 4)