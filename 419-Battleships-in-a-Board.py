#!/usr/bin/env python
# -*- coding: utf-8 -*-

# LeetCode with Python

# Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:
#
# You receive a valid board, made of only battleships or empty slots.
# Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
# At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
#
# Example:
# X..X
# ...X
# ...X
# In the above board there are 2 battleships.

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        h = len(board)
        w = len(board[0]) if h else 0
        count = 0
        for i in range(h):
            for j in range(w):
                if board[i][j] == 'X':
                    if i>0 and board[i-1][j]=='X':
                        continue
                    if j>0 and board[i][j-1]=='X':
                        continue
                    count += 1
        return count

if __name__ = '__main__':
	print Solution().countBattleships([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]])
