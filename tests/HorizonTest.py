#!/usr/bin/env python
#coding:utf-8

####################
#Unit test of Horizon.py
####################

import unittest
#moduel serach path
import pathconf

#テスト対象
import Horizon


class HorizonTest(unittest.TestCase):
    def test_hoge(self):
	self.assert_(False)


def suite():
    return unittest.TestSuite((
	unittest.makeSuite(HorizonTest,'test'),
	))
if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
