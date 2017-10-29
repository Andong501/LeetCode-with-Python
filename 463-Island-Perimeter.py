#!/usr/bin/env python
# -*- coding: utf-8 -*-

# LeetCode with Python

# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
#
# Example:
# Input:
# [[0,1,0,0],
# [1,1,1,0],
# [0,1,0,0],
# [1,1,0,0]]
# Output:
# 16

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        island_pos = [(i,j,item) for i,list in enumerate(grid) for j,item in enumerate(list) if item==1]
        total = len(island_pos)
        dup = 0
        for tuple in island_pos:
            r = tuple[0]
            c = tuple[1]
            if r:
                if grid[r-1][c] == 1:
                    dup += 1
            if r<len(grid)-1:
                if grid[r+1][c] == 1:
                    dup += 1
            if c:
                if grid[r][c-1] == 1:
                    dup += 1
            if c<len(grid[0])-1:
                if grid[r][c+1] == 1:
                    dup += 1
        return total*4-dup

if __name__ = '__main__':
	print Solution().islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])