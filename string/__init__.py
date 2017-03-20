#!/usr/bin/env python
# encoding: utf-8


"""
@version: 1.0
@author: xiaoqiangkx
@file: __init__.py.py
@time: 2017/3/20 14:04
@change_time: 
1.2017/3/20 14:04
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