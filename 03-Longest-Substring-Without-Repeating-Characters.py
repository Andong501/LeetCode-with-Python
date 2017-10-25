#!/usr/bin/env python
# -*- coding: utf-8 -*-

# LeetCode with Python

# Given a string, find the length of the longest substring without repeating characters.
#
# Example:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        left = 0
        res = 0
        for i, ch in enumerate(s):
            if (ch in dic) and (dic[ch]>=left):
                left = dic[ch] + 1
            dic[ch] = i
            res = max(res, i-left+1)
        return res

if __name__ = '__main__':
	print Solution().lengthOfLongestSubstring('pwwkew')