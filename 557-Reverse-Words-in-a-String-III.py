#!/usr/bin/env python
# -*- coding: utf-8 -*-

# LeetCode with Python

# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
#
# Example:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([w[::-1] for w in s.split()])

if __name__ = '__main__':
	print Solution().reverseWords("Let's take LeetCode contest")