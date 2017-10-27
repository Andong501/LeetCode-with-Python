#!/usr/bin/env python
# -*- coding: utf-8 -*-

# LeetCode with Python

# Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.
#
# Example:
# Input: 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

import math

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        bit = int(math.log(num, 2)) + 1 
        return num ^ 2**(bit)-1

if __name__ = '__main__':
	print Solution().findComplement(5)
