#!/usr/bin/env python
# -*- coding: utf-8 -*-

# LeetCode with Python

# Write a program that outputs the string representation of numbers from 1 to n.
# 
# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
#
# Example:
# n = 15,

# Return:
# [
#    "1",
#    "2",
#    "Fizz",
#    "4",
#    "Buzz",
#    "Fizz",
#    "7",
#    "8",
#    "Fizz",
#    "Buzz",
#    "11",
#    "Fizz",
#    "13",
#    "14",
#    "FizzBuzz"
# ]

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(1, n+1):
            if i%3 and i%5:
                res.append(str(i))
            elif i%5:
                res.append('Fizz')
            elif i%3:
                res.append('Buzz')
            else:
                res.append('FizzBuzz')
        return res

if __name__ = '__main__':
	print Solution().fizzBuzz(15)