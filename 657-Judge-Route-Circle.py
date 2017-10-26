#!/usr/bin/env python
# -*- coding: utf-8 -*-

# LeetCode with Python

# Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.
# 
# The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.
#
# Example1:
# 
# Input: "UD"
# Output: true
# 
# Example2:
# 
# Input: "LL"
# Output: false
#
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        u = 0
        d = 0
        l = 0
        r = 0
        for i in range(len(moves)):
            if moves[i] == 'U':
                u += 1
            elif moves[i] == 'D':
                d += 1
            elif moves[i] == 'L':
                l += 1
            else:
                r += 1
        return (u==d) and (l==r)
    
    def judgeCircle2(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return (moves.count('U')==moves.count('D')) and (moves.count('L')==moves.count('R'))

if __name__ = '__main__':
	print Solution().judgeCircle('UD')