#!/usr/bin/env python
# -*- coding: utf-8 -*-

# LeetCode with Python

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        lr = head
        charge = 0
        while(l1 or l2 or charge):
            sum, charge = charge, 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            if sum >= 10:
                charge = 1
                sum -= 10
            lr.next = ListNode(sum)
            lr = lr.next
        return head.next

if __name__ = '__main__':
	l1 = [2, 4, 3]
	l2 = [5, 6, 4]
	lr = Solution().addTwoNumbers(l1, l2)