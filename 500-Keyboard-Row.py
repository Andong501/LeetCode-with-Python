#!/usr/bin/env python
# -*- coding: utf-8 -*-

# LeetCode with Python

# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
#
# Example:
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        s = ['QWERTYUIOPqwertyuiop','ASDFGHJKLasdfghjkl','ZXCVBNMzxcvbnm']
        list = []
        for word in words:
            tag = 0
            for letter in word:
                if tag == 0:
                    if letter in s[0]:
                        tag = 1
                    if letter in s[1]:
                        tag = 2
                    if letter in s[2]:
                        tag = 3
                else:
                    if letter not in s[tag-1]:
                        tag = -1
                        break
            if tag != -1:
                list.append(word)
        return list

if __name__ = '__main__':
	print Solution().findwords(["Hello", "Alaska", "Dad", "Peace"])
