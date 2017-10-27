#!/usr/bin/env python
# -*- coding: utf-8 -*-

# LeetCode with Python

# Given two strings representing two complex numbers.

# You need to return a string representing their multiplication. Note i^2 = -1 according to the definition.
#
# Example:
# Input: "1+1i", "1+1i"
# Output: "0+2i"
# Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        lista = a.split('+')
        listb = b.split('+')
        a1 = int(lista[0])
        a2 = int(lista[1][:-1])
        b1 = int(listb[0])
        b2 = int(listb[1][:-1])
        c1 = a1 * b1
        c2 = a1 * b2 + a2 * b1
        c3 = a2 * b2
        res = str(c1-c3) + '+' + str(c2) + 'i'
        return res

if __name__ = '__main__':
	print Solution().complexNumberMultiply('1+1i', '1+1i')
