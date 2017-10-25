#!/usr/bin/env python
# -*- coding: utf-8 -*-

# LeetCode with Python

# TinyURL is a URL shortening service where you enter a URL such as
# 
# https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.
#
# Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work.
#
# You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
#

import random

class Codec:
    
    def __init__(self):
        self.dic = dict()
        self.dic_res = dict()

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        code = '0123456789abcdefghijklmnopqrstuvwsyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if (longUrl in self.dic):
            return 'http://tinyurl.com/' + self.dic[longUrl]
        
        else:
            value = ''.join(random.sample(code, 6))
            self.dic[longUrl] = value
            self.dic_res[value] = longUrl
            return 'http://tinyurl.com/' + self.dic[longUrl]

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.dic_res[shortUrl[-6:]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

if __name__ = '__main__':
	url = 'https://leetcode.com/problems/design-tinyurl'
	codec = Codec()
	print codec.decode(codec.encode(url))