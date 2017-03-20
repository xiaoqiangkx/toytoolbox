#!/usr/bin/env python
# encoding: utf-8


"""
@version: 1.0
@author: xiaoqiangkx
@file: test_string_utils.py
@time: 2017/3/20 14:09
@change_time: 
1.2017/3/20 14:09
"""
import unittest
from utils import convert


class TestUtilsString(unittest.TestCase):

	def test_to_str(self):
		self.assertIsInstance(convert.to_unicode("你好"), unicode, "should be unicode")
		self.assertIsInstance(convert.to_unicode(u"你好"), unicode, "should be unicode")
		self.assertIsInstance(convert.to_str("你好"), str, "should be str")
		self.assertIsInstance(convert.to_str(u"你好"), str, "should be str")
		return


if __name__ == '__main__':
	unittest.main()
