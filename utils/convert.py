#!/usr/bin/env python
# encoding: utf-8


"""
@version: 1.0
@author: xiaoqiangkx
@file: convert.py
@time: 2017/3/20 14:07
@change_time: 
1.2017/3/20 14:07
"""


def to_str(unicode_or_str):
	if isinstance(unicode_or_str, unicode):
		return unicode_or_str.encode("utf-8")
	else:
		return unicode_or_str


def to_unicode(unicode_or_str):
	if isinstance(unicode_or_str, str):
		return unicode_or_str.decode("utf-8")
	else:
		return unicode_or_str

if __name__ == '__main__':
	print to_unicode("我的世界观")
	print type(to_unicode("我的世界观"))