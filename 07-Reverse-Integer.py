#!/usr/bin/env python
# -*- coding: utf-8 -*-

# LeetCode with Python

# Reverse digits of an integer.
#
#The input and output are assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
#
# Example1: x = 123, return 321
# Example2: x = -123, return -321

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = 2147483647
        INT_MIN = -INT_MAX -1
        
        if (x>INT_MAX) | (x<INT_MIN):
            return 0
        else:
            px = abs(x)
            y = str(px)
            z = str()
            for i in range(len(y)-1, -1, -1):
                z += y[i]
            if x >= 0:
                return int(z) if int(z)<INT_MAX else 0
            else:
                return -int(z) if -int(z)>INT_MIN else 0

if __name__ = '__main__':
	print Solution().reverse(-123)